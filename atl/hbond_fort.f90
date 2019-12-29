subroutine calc_hbond_fort(file_name, donor_type, donor_typeH, acceptor_type, criteria, pbc_box, z_confined, dump_angle, frames)
! This subroutine calculates number of hydrogen bonds from .xyz format via averaging over specified frames.
implicit none
    
    ! arguments
    character(LEN=255), intent(in) :: file_name
    character(LEN=15), intent(in) :: donor_type, donor_typeH, acceptor_type ! e.g. 'O', 'H', 'O
    real*8, intent(in) :: criteria(3) ! H-bond criteria: rc_oo=3.6; rc_oh=10*2.5; ac_oho=30.
    integer, intent(in) :: frames(3)
    logical, intent(in) :: z_confined, dump_angle
    real*8, intent(in) :: pbc_box(3)

    INTEGER, PARAMETER :: MAXSIZE=200000
    REAL*8, PARAMETER :: RC_HH=1.3d0

    real*8 :: atoms_pos(MAXSIZE,3), dx, dy, dz
    character(LEN=15):: atoms_type(MAXSIZE)
    integer :: current_frame, read_frame, start_frame, stop_frame, step_frame
    integer :: i, j, k, l, io, jo, jh
    integer :: donor(MAXSIZE), acceptor(MAXSIZE), n_donor, n_acceptor
    integer :: neigh(2), nh
    real*8 :: r2, ra(3), rb(3), dot, s1, s2, arg, angle, nHB
    integer :: nHB_i
    real*8 :: rc_OO, rc_OH, ac_OHO
    integer :: nAtoms

    ! opennig files
    open(1, file=trim(file_name), status='OLD')
    open(4, file='hb.dat', status='UNKNOWN')
    if (dump_angle) open(2,file='angle.dat', status='UNKNOWN')

    ! set HB's criteria
    rc_OO = criteria(1)
    rc_OH = criteria(2)
    ac_OHO = criteria(3) 

    ! setting frames
    start_frame = frames(1)
    stop_frame = frames(2)
    step_frame = frames(3)
    
    ! =======================

    ! write(*,*)
    ! write(*,'(A15,3F8.3)') 'PBC Box      :', pbc_box(1), pbc_box(2), pbc_box(3)
    ! write(*,*) 'donor(O)     :', donor_type
    ! write(*,*) 'donor(H)     :', donor_typeH
    ! write(*,*) 'acceptor(O)  :', acceptor_type
    ! write(*,*) 'z-confined   :', z_confined
    ! write(*,*) 'start frame  :', start_frame
    ! write(*,*) 'stop frame   :', stop_frame
    ! write(*,*) 'step frame   :', step_frame

    ! =======================

    atoms_pos = 0.0d0
    read_frame = 0
    current_frame = 0

    do while (.true.)

        read(1, *, IOSTAT=io) natoms
        if (io.lt.0) exit
        read(1, *)  ! read comment line

        current_frame = current_frame + 1

        if (current_frame.ge.start_frame .and. mod(current_frame, step_frame).eq.0 .and. current_frame.le.stop_frame) then

            read_frame = read_frame + 1

            !if (read_frame == 1) write(*,*) "N atoms:", natoms
            ! loop over all atoms and reading atomic types and positions
            do i = 1, natoms
                read(1,*) atoms_type(i), atoms_pos(i,1), atoms_pos(i,2), atoms_pos(i,3)
            enddo

            ! =======================================
        
            n_acceptor = 0
            do i=1, nAtoms 
                if ( atoms_type(i).eq.acceptor_type ) then
                    n_acceptor = n_acceptor+1
                    acceptor(n_acceptor) = i
                endif
            enddo
                
            n_donor = 0 
            do i=1, nAtoms           
                if ( atoms_type(i).eq.donor_type ) then
                        n_donor = n_donor+1
                        donor(n_donor) = i 
                endif
            enddo   
                
            ! ---------------------------------------- 

            nHB = 0.0
            do i=1, n_acceptor 
                
                nHB_i = 0  ! number of HBs for each acceptor
                io=acceptor(i)

                do j=1, n_donor 
                    
                    jo = donor(j)
                    if ( io.eq.jo) cycle                                 
                                    
                    ! donor-acceptor distance (O-O)
                    ! ------------------------------------
                    dx = atoms_pos(io,1) - atoms_pos(jo,1)
                    dy = atoms_pos(io,2) - atoms_pos(jo,2)
                    dz = atoms_pos(io,3) - atoms_pos(jo,3)
                    ! ---
                    call apply_pbc(pbc_box(1), dx)
                    call apply_pbc(pbc_box(2), dy)
                    if (.not.z_confined) then
                        call apply_pbc(pbc_box(3), dz)
                    endif
                    r2 = dx*dx + dy*dy + dz*dz
                    ! -----------------------------------
                
                    if (r2<rc_oo*rc_oo) then
                        
                        ! find bonded hydrogens for a donor
                        nh = 0 
                        do k=1, nAtoms    

                            if ( atoms_type(k).eq.donor_typeH ) then 
                            
                                ! O-H distance (hydrogen of Donor)
                                ! ----------------------
                                dx = atoms_pos(k,1) - atoms_pos(jo,1)
                                dy = atoms_pos(k,2) - atoms_pos(jo,2)
                                dz = atoms_pos(k,3) - atoms_pos(jo,3)
                                ! ---
                                call apply_pbc(pbc_box(1), dx)
                                call apply_pbc(pbc_box(2), dy)
                                if (.not.z_confined) then
                                    call apply_pbc(pbc_box(3), dz)
                                endif
                                r2 = dx*dx + dy*dy + dz*dz
                                ! ----------------------

                                ! bonded-H
                                if (r2 < RC_HH*RC_HH) then
                                    nh = nh + 1
                                    neigh(nh) = k
                                endif            

                                if (nh.gt.2) then
                                    write(*,*) 'WARNING: more than 2 neighboers, truncated!'
                                    exit    
                                endif

                            endif               
                        enddo
                                    
                        ! O(donor)-H distance                                                
                        do l=1,nh       

                            jh=neigh(l)
                            ! O-H distace
                            dx = atoms_pos(jh, 1)-atoms_pos(jo, 1)
                            dy = atoms_pos(jh, 2)-atoms_pos(jo, 2)
                            dz = atoms_pos(jh, 3)-atoms_pos(jo, 3)
                            ! ---
                            call apply_pbc(pbc_box(1), dx)
                            call apply_pbc(pbc_box(2), dy)
                            if (.not.z_confined) then
                                call apply_pbc(pbc_box(3), dz)
                            endif
                            r2= dx*dx  + dy*dy + dz*dz
                            ! ----------------------------
                            
                            if (r2<rc_oh*rc_oh) then
                                
                                !OH-O angle                                            
                                ra(1)=atoms_pos(io, 1)-atoms_pos(jo, 1); 
                                ra(2)=atoms_pos(io, 2)-atoms_pos(jo, 2); 
                                ra(3)=atoms_pos(io, 3)-atoms_pos(jo, 3);
                                
                                rb(1)=atoms_pos(jh, 1)-atoms_pos(jo, 1); 
                                rb(2)=atoms_pos(jh, 2)-atoms_pos(jo, 2); 
                                rb(3)=atoms_pos(jh, 3)-atoms_pos(jo, 3);                                                   
                                
                                dot=0.d0; s1=0.d0; s2=0.d0
                                do k=1,3                       
                                    dot=dot+ra(k)*rb(k)
                                    s1=s1+ra(k)**2
                                    s2=s2+rb(k)**2
                                enddo
                                arg=dot/SQRT(s1)/SQRT(s2)
                                angle=ACOS(arg)*57.296d0; 
                                !write(*,*) angle
                                
                                if (angle<ac_oho) then                            
                                    nHB_i=nHB_i+1 !counting HB 
                                endif

                                ! dump angle into the file
                                if (dump_angle) write(2,'(1F10.5)') angle
            
                            endif
                        enddo                 
                    endif              
                enddo
                
                ! add number of an acceptor's HB to total number of HB
                nHB=nHB+nHB_i
            
            enddo   

                                
        nHB=nHB;   
        !write(*,*) "nAtoms:",nAtoms
        ! write(*,'(I5,1F10.5,2I5)') current_frame, nHB, n_acceptor, n_donor
        write(4,'(I5,1F10.5,2I5)') current_frame, nHB, n_acceptor, n_donor
        !exit
        
        ! ----------------------------------------------
            else
                do i = 1, natoms ! natoms & comment line
                        read(1,*) !t, x, y, z
                enddo
            endif
    
        enddo
        close(1)
        close(4)
        if (dump_angle) close(2)
    
        ! -----------------------------------------------
        ! write(*,*) 'total frame', current_frame
        ! write(*,*) 'frame equilibrium', start_frame
        ! write(*,*) 'total readed frame', read_frame
        !write(*,*) "subroutine run succesfully."
    
end subroutine calc_hbond_fort

! ===========================================

subroutine apply_pbc(length, dist)
    ! applying pbc along the specified direction
    implicit none
    real*8, intent(in) :: length
    real*8, intent(inout) :: dist
    if (length .gt. 1.0d-3) then  ! skip 0 size box length

        if (dist .gt.  length*0.5d0) dist = dist - length
        if (dist .lt. -length*0.5d0) dist = dist + length
    endif
end subroutine apply_pbc

! ===========================================

! function calc_r2(atoms_pos, pbc_box, z_confined) result(r2)
!     ! calculate sqaure of distance while applying PBC.
!     implicit none
!     real*8, intent(in) :: dx, dy, dz, pbc_box(3)
!     real*8 :: r2
!     logical :: z_confined

!     call apply_pbc(pbc_box(1), dx)
!     call apply_pbc(pbc_box(2), dy)
!     if (.not.z_confined) then
!         call apply_pbc(pbc_box(3), dz)
!     endif
!     r2 = dx*dx + dy*dy + dz*dz
! end function calc_r2

! ===========================================

! program hydrogen_bond
! implicit none

! character(len=255) :: file_name
! character(len=15) :: donor_type, donor_typeH, acceptor_type
! real*8 :: criteria(3), pbc_box(3)
! logical :: z_confined
! integer :: frames(3)

! file_name = 'dump.xyz'
! donor_type = '2'
! donor_typeH = '1'
! acceptor_type = '2'
! criteria = (/3.2d0, 25.d0, 30d0/)
! pbc_box = (/19.246222, 19.246222, 19.246222/)
! z_confined = .false.
! frames = (/10, 10000, 1/)

! call calc_hbond_fort(file_name, donor_type, donor_typeH, acceptor_type, criteria, pbc_box, z_confined, frames)

! end program hydrogen_bond




