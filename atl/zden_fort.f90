subroutine calc_zden_fort(file_name, sel_type, zlim, nz, frames)
! This subroutine calculates density profile along z-axis 
! from .xyz format via averaging over specified frames.
implicit none

    ! arguments
    character(LEN=15), intent(in) :: file_name
    character(LEN=15), intent(in) :: sel_type
    real*8, intent(in) :: zlim(2)
    integer, intent(in) :: nz
    integer, intent(in) :: frames(3)

    INTEGER, PARAMETER :: MAXSIZE=200000, MESHSIZE=5000

    ! local variables
    real*8 :: atoms_pos(MAXSIZE,3)
    real*8 :: z(MESHSIZE), den_z(MESHSIZE)
    real*8 :: dz, zi, coef
    real*8 :: zmin, zmax
    character(LEN=15):: atoms_type(MAXSIZE)
    integer :: natoms, i, j
    integer :: nsel, sel(MAXSIZE)
    integer :: current_frame, read_frame, start_frame, stop_frame, step_frame
    integer :: io

    ! opennig files
    open(1,file=trim(file_name), status='old')

    ! setting frames
    start_frame = frames(1)
    stop_frame = frames(2)
    step_frame = frames(3)

    ! =======================

    ! write(*,*) '---------'
    ! write(*,*) file_name
    ! write(*,*) box_area
    ! write(*,*) sel_type
    ! write(*,*) start_frame
    ! write(*,*) stop_frame
    ! write(*,*) step_frame
    ! write(*,*) '---------'

    ! =======================

    zmin = zlim(1)
    zmax = zlim(2)
    dz = (zmax-zmin)/nz
    ! write(*,*) "delta_z:", dz
    ! write(*,*) "zmin zmax:", zmin, zmax

    do i = 1, nz+1
      z(i) = zmin + dz*(i-1);
    enddo

    ! initialize g(r) to zero
    den_z = 0.0d0

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

            ! -------------------------------------

            nsel = 0;
            do i = 1, natoms
                if( trim(atoms_type(i)) == sel_type ) then !atom selection
                    nsel = nsel + 1
                    sel(nsel) = i
                endif
            enddo
            ! if (current_frame == start_frame) write(*,*) 'Selected atoms', nsel

            ! -------------------------------------

            do i = 1, nsel
                zi = atoms_pos(sel(i),3)
                do j = 1, nz
                    if ( zi.ge.z(j) .and. zi.lt.z(j+1) ) then
                        den_z(j) = den_z(j) + 1.0D0
                        exit
                    endif
                enddo
            enddo

        else
            do i = 1, natoms ! natoms & comment line
                    read(1,*) !t, x, y, z
            enddo
        endif

    enddo
    close(1)

    ! write(*,*) 'total frame', current_frame
    ! write(*,*) 'frame equilibrium', start_frame
    ! write(*,*) 'total readed frame', read_frame

    ! ------------------------------

    coef = 1.0D0/(dz*read_frame)
    do i = 1, nz
      z(i) = (z(i)+z(i+1))*0.5d0
      den_z(i) = den_z(i)*coef 
    enddo

    ! ------------------------------

    open(4,file='zden.dat', status='unknown')
    do i = 1, nz
        write(4,'(2F16.7)') z(i), den_z(i)
    enddo
    close(4)

	! ------------------------------

    !write(*,*) "subroutine run succesfully."

end subroutine calc_zden_fort


! program density_profile
! implicit none

!    real*8 ::  zlim(2)
!    integer :: nz, frames(3)
!    character(LEN=15) :: sel_type, file_name

!    nz = 200
!    zlim = (/0, 15/)
!    frames = (/1, 10000, 1/)
!    sel_type = 'O'
!    file_name = 'dump.xyz'

!    call calc_zden_fort(file_name, sel_type, zlim, nz, frames)

! end program density_profile
