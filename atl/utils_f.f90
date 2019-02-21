
program radial_distribution_function
implicit none

    real*8 ::  pbc_box(3), rmax, delta_z
    integer :: nr, start_frame, stop_frame, step_frame
    logical :: lateral
    character(LEN=15) :: sel_type, file_name

    pbc_box = (/19.246222, 19.246222, 19.246222/)
    nr=100
    rmax=9.5
    start_frame = 50
    stop_frame = 1000000
    step_frame = 1
    lateral=.false.
    delta_z=1.0
    sel_type='2'
    file_name='dump.xyz'

    call calculate_rdf_f(file_name, pbc_box, nr, rmax, lateral, delta_z, sel_type, start_frame, stop_frame, step_frame)

end program radial_distribution_function


subroutine calculate_rdf_f(file_name, box, nr, rmax, lateral, delta_z, sel_type, start_frame, stop_frame, step_frame)
implicit none

    ! arguments
    character(LEN=15), intent(in) :: file_name
    real*8, intent(in) :: box(3)
    integer, intent(in) :: nr
    real*8, intent(in) :: rmax, delta_z
    logical, intent(in) :: lateral
    character(LEN=15), intent(in) :: sel_type

    INTEGER, PARAMETER :: MAXSIZE=200000, MESHSIZE=5000
    REAL*8, PARAMETER :: PI=3.141592d0

    ! local variables
    real*8 :: atoms_pos(3, MAXSIZE)
    character(LEN=15):: atoms_type(MAXSIZE)
    real*8 :: dr, r(MESHSIZE), g_r(MESHSIZE), rij, dx ,dy , dz, rho
    integer :: natoms, i, j, nsel, ind, sel(MAXSIZE)
    integer :: current_frame, read_frame, start_frame, stop_frame, step_frame
    integer :: n, io

    ! opennig files
    open(1,file=trim(file_name), status='old')
    open(4,file='gr.dat', status='unknown')

    write(*,*) 'call subroutine'

    ! =======================

    dr = rmax/float(nr);
    do i= 1, nr+1
      r(i) = dr*(i-1);
    enddo
    g_r=0.0d0

    write(*,'(A,2F5.2,I5)') 'r dr nr ', rmax , dr, nr

    ! =======================

    atoms_pos = 0.0d0
    read_frame = 0
    current_frame = 0

    do while (.true.)

        current_frame = current_frame + 1

        if (current_frame>=start_frame .and. mod(current_frame, step_frame).eq.0 .and. current_frame.le.stop_frame) then

            read_frame = read_frame + 1

            read(1,*,IOSTAT=io) natoms
            if (io<0) exit
            read(1, *)  ! read next line
            ! loop over all atoms and reading atomic types and positions
            do n=1,natoms
                read(1,*) atoms_type(n), atoms_pos(n,1), atoms_pos(n,2), atoms_pos(n,3)
            enddo

            ! -------------------------------------

            nsel = 0
            do i = 1, natoms
              if( trim(atoms_type(i)) == sel_type ) then !atom selection
                nsel = nsel + 1
                sel(nsel) = i
              endif
            enddo

            if (current_frame==start_frame) write(*,*) 'Selected atoms', nsel

            ! -------------------------------------

            do i = 1, nsel

              do j = 1, nsel

                    if (i == j) cycle  ! exclude self-counting

                    ! applying PBC
                    dx = atoms_pos(sel(i),1) - atoms_pos(sel(j),1)
                    if (dx.gt.box(1)*0.5d0)  dx = dx - box(1)
                    if (dx.lt.-box(1)*0.5d0) dx = dx + box(1)
                    ! ---
                    dy = atoms_pos(sel(i),2) - atoms_pos(sel(j),2)
                    if (dy.gt.box(2)*0.5d0)  dy = dy - box(2)
                    if (dy.lt.-box(2)*0.5d0) dy = dy + box(2)
                    ! ---
                    if (.not.lateral) then
                        dz = atoms_pos(sel(i),3) - atoms_pos(sel(j),3)
                        if (dz.gt.box(3)*0.5d0)  dz = dz - box(3)
                        if (dz.lt.-box(3)*0.5d0) dz = dz + box(3)
                    endif

                    ! ----------------------

                    if (.not.lateral) then
                        rij = sqrt( dx**2 + dy**2 + dz**2 )
                        ind = int(rij/dr)+1
                        g_r(ind) = g_r(ind)+1.d0

                    else
                        if( abs(atoms_pos(sel(i),3) - atoms_pos(sel(j),3)).lt.0.5d0*delta_z ) then
                        rij = sqrt( dx**2 + dy**2 )
                        ind = int(rij/dr) + 1
                        g_r(ind)=g_r(ind) + 1.d0
                        endif
                endif

              enddo

            enddo

        else
            do i = 1, natoms
                    read(1,*) !t, x, y, z
            enddo
        endif

    enddo

    write(*,*) 'total frame', current_frame
    write(*,*) 'frame equilibrium', start_frame
    write(*,*) 'total readed frame', read_frame
    Write(*,*) 'lateral RDF: ', lateral

    ! ------------------------------

    rho = float(nsel)/(box(1)*box(2)*box(3))
    write(*,*) "n-density", rho

    do i = 1, nr

      r(i) = (r(i)+r(i+1))*0.5d0
      g_r(i) = g_r(i)/n

      if (.not.lateral) then
        g_r(i) = g_r(i)/( PI*4./3.*(r(i+1)**3-r(i)**3) )/rho/nsel/2

      else
        g_r(i) = g_r(i)/( PI*( r(i+1)**2-r(i)**2)*delta_z )/rho/nsel/2
      endif

    enddo

    ! ------------------------------

    do i = 1, nr
        write(4,'(2F16.7)') r(i), g_r(i)
    enddo

end subroutine calculate_rdf_f

