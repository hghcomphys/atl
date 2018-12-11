
class MolecularFrame(object):
    """
    This class works with lammps input format in form of a molecular frame.
    
    Example
    
        water = MolecularFrame()
        water.read_lmp('lammps.lmp')
        print  water
        water.shift_atoms_id(1000)
        water.write_lmp('out.lmp')


    Not implemented yet:
    *** comments
    *** tilted unit cell
    """
    
    # atoms, angles, bonds, dihedrals
    # n_atoms, n_angles, n_bonds, n_dihedrals
    # move, center
    # read (lmp,xyz,pdb)
    # set,get (charge,mass,aid,mid)
    # keep_block, keep_cylinder
    # del_block, del_cylinder
    # replace_mol, replace_atom   
    # replicate, recenter
    
    # Box:       [[Lx],[Ly],[Lz]]
    # Masses:    [atype,mass]
    # Atoms:     [aid,mid,atype,charge,xpos,ypos,zpos,imx,imy,imz,type]
    # Bonds:     [bid,btype,aid,aid]
    # Angles:    [anid,antype,aid,aid,aid]
    # Dihedrals: [did,dtype,aid,aid,aid,aid]
    # Impropers: [did,dtype,aid,aid,aid,aid]
    

    # ====================================================================================================

    def __init__(self, attributes='Box Masses Atoms Bonds Angles Dihedrals Impropers Types', molframe={}):
        
        import copy
        self._attributes = attributes    
        self._molframe = copy.deepcopy( molframe )
        
          
    def __str__(self):
        """
        This function returns a string includes general attributes of the molecular frame
        such as number of atoms, molecules, types, etc.

        """
        out='Molecular Frame\n---------------\n'
        for k in self._molframe.keys():
            out += '%d '%len(self._molframe[k]) + k + '\n'
        out += '%d Molecules'%self.n_molecules
        return out
    
        
    def __clean_molframe(self):
        """
        This function cleans all data from the molecular frame.

        """
        for k in self._attributes.split():
            self._molframe[k] = []

    # ====================================================================================================

    @property
    def n_atoms(self):     
        return len(self._molframe['Atoms'])
    
    @property
    def n_bonds(self):     
        return len(self._molframe['Bonds'])
    
    @property
    def n_angles(self):     
        return len(self._molframe['Angles'])
       
    @property
    def n_dihedrals(self):     
        return len(self._molframe['Dihedrals'])
    
    @property
    def n_impropers(self):     
        return len(self._molframe['Impropers']) 
    
    @property
    def lx(self):     
        return (self._molframe['Box'][0][1] - self._molframe['Box'][0][0])

    @property
    def xlo(self):
        return self._molframe['Box'][0][0]

    @property
    def xlh(self):
        return self._molframe['Box'][0][1]
    
    @property
    def ly(self):     
        return (self._molframe['Box'][1][1] - self._molframe['Box'][1][0])

    @property
    def ylo(self):
        return self._molframe['Box'][1][0]

    @property
    def ylh(self):
        return self._molframe['Box'][1][1]
    
    @property
    def lz(self):     
        return (self._molframe['Box'][2][1] - self._molframe['Box'][2][0])

    @property
    def zlo(self):
        return self._molframe['Box'][2][0]

    @property
    def zlh(self):
        return self._molframe['Box'][2][1]
    
    @property
    def box(self):     
        return self.lx, self.ly, self.lz
    
    @property
    def atom_types(self):     
        return self._molframe['Types'][0]

    @property
    def bond_types(self):
        return self._molframe['Types'][1]

    @property
    def angle_types(self):
        return self._molframe['Types'][2]

    @property
    def dihedral_types(self):
        return self._molframe['Types'][3]

    @property
    def improper_types(self):
        return self._molframe['Types'][3]


    # ====================================================================================================
    # Removing atoms and molecuels
    # ====================================================================================================

    def _remove_aid(self, aid, section, index=[]):
        removed_sec = []
        for sec in self._molframe[section]:
            for i in index:
                if aid == sec[i]:
                    removed_sec.append(sec)
        for sec in removed_sec:
            self._molframe[section].remove(sec)


    def remove_atoms(self, aid_list=[]):
        for aid in aid_list:
            self._remove_aid(aid, 'Atoms', index=[0])
            self._remove_aid(aid, 'Bonds', index=[2, 3])
            self._remove_aid(aid, 'Angles', index=[2, 3, 4])
            self._remove_aid(aid, 'Dihedrals', index=[2, 3, 4, 5])
            self._remove_aid(aid, 'Impropers', index=[2, 3, 4, 5])


    def remove_molecules(self, mid_list=[]):
        for mid in mid_list:
            molecule = self._find_molecule(mid)
            self.remove_atoms(molecule)
        # has to be used cautiously at top-layer functions
        self.reset_aid()
        self.reset_mid()


    # ====================================================================================================
    # Resetting aid & mid
    # ====================================================================================================

    def _replace_aid(self, aid_old, aid_new, section, index=[]):
        for j in range(len(self._molframe[section])):
            if not section in 'Atoms':
                self._molframe[section][j][0] = j + 1
            for i in index:
                for k in range(self.n_atoms):
                    if aid_old[k] == self._molframe[section][j][i]:
                        self._molframe[section][j][i] = aid_new[k]
                        break


    def reset_aid(self):
        aid_old = [at[0] for at in self._molframe['Atoms']]
        aid_new = [i+1 for i in range(self.n_atoms)]
        self._replace_aid(aid_old, aid_new, 'Atoms', index=[0])
        self._replace_aid(aid_old, aid_new, 'Bonds', index=[2, 3])
        self._replace_aid(aid_old, aid_new, 'Angles', index=[2, 3, 4])
        self._replace_aid(aid_old, aid_new, 'Dihedrals', index=[2, 3, 4, 5])
        self._replace_aid(aid_old, aid_new, 'Impropers', index=[2, 3, 4, 5])



    def reset_mid(self):
        mid_list = self.mid
        for i in range(self.n_atoms):
            for j in range(len(mid_list)):
                if self._molframe['Atoms'][i][1] == mid_list[j]:
                    self._molframe['Atoms'][i][1] = j + 1
                    break


    # ====================================================================================================
    # Molecular properties
    # ====================================================================================================

    @property
    def mid(self):
        mid_list = []
        for i in range(self.n_atoms):
            if not self._molframe['Atoms'][i][1] in mid_list:
                mid_list.append(self._molframe['Atoms'][i][1])
        mid_list.sort()
        return mid_list

    @property
    def aid(self):
        aid_list = []
        for i in range(self.n_atoms):
            aid_list.append(self._molframe['Atoms'][i][0])
        aid_list.sort()
        return aid_list

    @property
    def n_molecules(self):
        return len(self.mid)


    # ====================================================================================================
    # find functions
    # ====================================================================================================

    def _find_atom(self, aid=None):
        # assert (aid!=None), "Specify atom id!"
        atom = None
        for at in self._molframe['Atoms']:
            if aid==at[0]:
                atom = at
                break
        # assert (atom!=None), "No atom was found with specified aid!"
        return atom


    def _find_molecule(self, mid):
        # assert (mid != None), "Specify molecule id!"
        molecule = []
        for at in self._molframe['Atoms']:
            if mid == at[1]:
                molecule.append(at[0])
        # assert (molecule!=[]), "No molecule was found with specified mid!"
        return molecule


    def _find_aids_for_mid(self):
        mid_list = self.mid
        molecule_list = {}
        for mid in mid_list:
            molecule_list['mid_%d' % mid]=self._find_molecule(mid)
        return molecule_list


    # ====================================================================================================
    # select molecules
    # ====================================================================================================

    def select_molecules_in_region(self, region_func=None):
        removed_mid = []
        mid_list = self.mid
        for mid in mid_list:
            molecule = self._find_molecule(mid)
            for aid in molecule:
                atom = self._find_atom(aid)
                xpos = atom[4]
                ypos = atom[5]
                zpos = atom[6]
                if not region_func(xpos,ypos,zpos):
                    removed_mid.append(mid)
                    break

        new_mf = MolecularFrame(attributes=self._attributes, molframe=self._molframe)
        new_mf.remove_molecules(removed_mid)
        return new_mf


    def select_molecules_randomly(self, frac=1.0, nmol=None, seed=None):
        import numpy
        if not seed is None:
            numpy.random.seed(seed)
        if not nmol is None:
            nsample = nmol
        else:
            nsample = int((1.-frac) * self.n_molecules)
        mid_list = self.mid
        removed_mid = list(numpy.random.choice(mid_list, nsample))

        new_mf = MolecularFrame(attributes=self._attributes, molframe=self._molframe)
        new_mf.remove_molecules(removed_mid)
        return new_mf


    # ====================================================================================================
    # swap molecules
    # ====================================================================================================

    # def swap_molecules_randomly(self, molecule, frac=1.0, seed=None):
    #
    #     import numpy
    #     if not seed is None:
    #         numpy.random.seed(seed)
    #     nsample = int(frac * self.n_molecules)
    #
    #     mid_list = self.mid
    #     removed_mid = list(numpy.random.choice(mid_list, nsample))
    #
    #
    #     new_mf = MolecularFrame(attributes=self._attributes, molframe=self._molframe)
    #     new_mf.remove_molecules(removed_mid)
    #
    #     for i in range(nsample):
    #         inserted_mol = numpy.random.choice(molecule.mid)
    #
    #     return new_mf


    # ====================================================================================================
    # replicating molframe
    # ====================================================================================================

    # def replicate(self, n=[1, 1, 1]):
    #     for nx in range(n[0]):
    #         for ny in range(n[1]):
    #             for nz in range(n[2]):
    #
    #                 self._molframe



    # ====================================================================================================
    # read/write .xyz format
    # ====================================================================================================

    def read_xyz(self, filename, frame=-1):
        
        self.__clean_molframe()
        
        import atl.io as io #!!!
        data = io.read_xyz(filename, frame)  
        
        aid=1; mid=1
        for d in data:

            #      [aid, mid, atype, charge, xpos, ypos, zpos, imx, imy, imz, type]
            atom = [aid, mid, 0    , 0.0   , d[1], d[2], d[3], 0  , 0  , 0  , d[0] ]

            self._molframe['Atoms'].append( atom )
            aid += 1
            mid += 1
   

    def write_xyz(self, filename):             
        with open(filename, 'w') as fo:
            # import datetime
            # fo.write('ATL dump %s\n' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            fo.write('%d\nGenerated by ATL\n'%self.n_atoms)
            for at in self._molframe['Atoms']:
                fo.write('%s %f %f %f\n'%(at[10],at[4],at[5],at[6]))


    # ====================================================================================================
    # read/write lammps format
    # ====================================================================================================

    def read_lmp(self,filename):
        self.__clean_molframe()
        from lammps_input import read_lammps_input
        data=read_lammps_input(filename, self._attributes)
        for k in data.keys():
            self._molframe[k] = data[k]
    
    
    def write_lmp(self, filename):
        from lammps_input import write_lammps_input
        write_lammps_input(filename, self._molframe)


    # ====================================================================================================
    # Merging two molecules
    # ====================================================================================================

    def __add__(self, other):
        
        # first step just merging two molecules without common atomic types
        # then function that merges two atomic types
        # mass values are usfule to identify atomic types

        molframe = {}     
        for attribute in self._attributes.split():
            
            if attribute == 'Boxes':
                molframe[attribute] = self._molframe[attribute] # taking boxsize from first object

            elif attribute == 'Types':
                molframe[attribute] = [ x+y for x,y in zip(self._molframe[attribute], other._molframe[attribute]) ]

            else:
                tmp_list = [self._molframe[attribute], other._molframe[attribute]]
                molframe[attribute] = reduce(lambda x,y: x+y, tmp_list)
            
        return MolecularFrame(attributes=self._attributes,molframe=molframe)


    # ====================================================================================================
    # Shifting ids
    # ====================================================================================================

    def __shift_id(self, attribute, columns, shift_id):
        for mf in self._molframe[attribute]:
            for i in range(columns[0], columns[1]):
                mf[i] += shift_id
                
   
    def shift_atoms_id(self, shift_id=0):        
        self.__shift_id('Atoms',     [0,1], shift_id)
        self.__shift_id('Bonds',     [2,4], shift_id)
        self.__shift_id('Angles',    [2,5], shift_id)
        self.__shift_id('Dihedrals', [2,6], shift_id)
        self.__shift_id('Impropers', [2,6], shift_id)
                
    
    def shift_bonds_id(self, shift_id=0):
        self.__shift_id('Bonds', [0,1], shift_id)
    
    
    def shift_angles_id(self, shift_id=0):
        self.__shift_id('Angles', [0,1], shift_id)
            
    
    def shift_dihedrals_id(self, shift_id=0):
        self.__shift_id('Dihedrals', [0,1], shift_id)
    

    def shift_impropers_id(self, shift_id=0):
        self.__shift_id('Impropers', [0,1], shift_id)
        
        
    def shift_mols_id(self, shift_id=0):
        self.__shift_id('Atoms', [1,2], shift_id)
    
           
    def shift_atom_types(self, shift_id=0):
        self.__shift_id('Atoms',  [2,3], shift_id)
        self.__shift_id('Masses', [0,1], shift_id)
    
    
    def shift_bond_types(self, shift_id=0):
        self.__shift_id('Bonds', [1,2], shift_id)
    
    
    def shift_angle_types(self, shift_id=0):
        self.__shift_id('Angles', [1,2], shift_id)
    
    
    def shift_dihedral_types(self, shift_id=0):
        self.__shift_id('Dihedrals', [1,2], shift_id)
    
    
    def shift_improper_types(self, shift_id=0):
        self.__shift_id('Impropers', [1,2], shift_id)


    # ====================================================================================================
    # Setting properties
    # ====================================================================================================


    # ====================================================================================================
    # Moving Atoms
    # ====================================================================================================

    def move_atoms(self, move=[0.,0.,0.], box=False):
        # Atoms
        for atom in self._molframe['Atoms']:
            for i in range(3):
                atom[i+4] += move[i] # xpos,ypos,zpos
        # Box
        if box:
            for i in range(3):
                for j in range(2):
                    self._molframe['Box'][i][j] += move[i]


    @property
    def total_mass(self):
        mass = 0
        for at in self._molframe['Atoms']:
            mass += self._molframe['Masses'][at[2]][1]
        return mass


    @property
    def ceter_of_mass(self):
        rcm = [0., 0., 0.]
        for at in self._molframe['Atoms']:
            mass = self._molframe['Masses'][at[2]][1]
            for i in range(3):
                rcm[i] += mass*at[i+4]
        for i in range(3):
            rcm[i] /= self.total_mass
        return rcm


    def recenter(self, center=[0.,0.,0.], box=True):
        rcm = self.ceter_of_mass
        self.move_atoms(move=[-r+c for r,c in zip(rcm,center)], box=box)



    # ====================================================================================================
    # Water tip3p (adding bonds and angles)
    # ====================================================================================================

    def apply_tip3p(self, O_type, mol_id=0):
        """
        This function adds to molecular frame bond and angle information of identified water molecules
        that is determined by a input argument. Importantly, It assumes that each water oxygen in atomic section
        is followed by two hydrogen atoms. It increases the number of bond and angle types by one.

        Example:

            mf = MolecularFrame()
            mf.read_lmp('../grn-wt-h9.3.lmp') # without water bonds & angles
            mf.apply_tip3p(O_type=3,mol_id=1) # adding bonds and angles
            mf.write_lmp('../out.lmp')
        """

        mid = mol_id
        self._molframe['Types'][1] += 1 # ading bond type
        self._molframe['Types'][2] += 1 # ading angle type

        for n in range(self.n_atoms):

            if self._molframe['Atoms'][n][2] != O_type: continue;  # only water oxygen

            # Atoms
            mid+=1
            for i in range(3):
                self._molframe['Atoms'][n+i][1] = mid

            # Bonds
            for i in range(2):
                self._molframe['Bonds'].append([self.n_bonds+1, self.bond_types,
                                                self._molframe['Atoms'][n][0],
                                                self._molframe['Atoms'][n+i+1][0]])
            # Angles
            self._molframe['Angles'].append([self.n_angles+1, self.angle_types,
                                             self._molframe['Atoms'][n+1][0],
                                             self._molframe['Atoms'][n][0],
                                             self._molframe['Atoms'][n+2][0]])
