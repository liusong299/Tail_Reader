'''
--------------------------------------------------------------------------------
--                Tails Reader V0.1 by Stephen Liu 20/09/2014                 --
--                        stephenliu1989@gmail.com                            --
--------------------------------------------------------------------------------
-- This Program will read files with same extension tail in a folder          --
-- Example:                                                                   --
-- If you want read all *.txt files in 'Myfolder/' folder, and write all the  --
-- tails in a file called 'TXT_Tail.out'                                      --
--                                                                            --
-- You can use this program like this:                                        --
-- > python Tails_Reader.py Myfolder txt TXT_tail                              --
--                                                                            --
-- Good luck!                                                                 --
-- Stephen Liu                                                                --
-- stephenliu1989@gmail.com                                                   --
--------------------------------------------------------------------------------
'''

import os
import subprocess
import sys

def walk_dir(input_traj_dir,input_traj_ext,topdown=True):
    frame_list = []
    for root, dirs, files in os.walk(input_traj_dir, topdown):
        for name in files:
            if os.path.splitext(name)[1] == input_traj_ext:
                frame_list.append( os.path.join( root, name ))
    return frame_list

def get_trajlist(trajlist_filename, trajlist_dir):
    trajlist_file = open( trajlist_filename )
    trajlist_list = []
    for line in trajlist_file:
        #print line
        list = trajlist_dir + '/' + line.rstrip("\n")
        trajlist_list.append( list )
    trajlist_file.close()
    return trajlist_list

def get_homedir():
    return os.getcwd()

def get_atom_indices(indices_filename, indices_dir ):
    indices_file = open( indices_dir + '/' + indices_filename )
    atom_indices = map(int, indices_file.read().split(' '))
    indices_file.close()
    del atom_indices[ 0 ]
    return atom_indices


def get_framelist( trajlist ):
    framelist = []
    framelist.extend( walk_dir( trajlist, '.txt'))
    return framelist

# int main()
# I just want it looks like a head  >_<
# and tell you this program begin from here:

input_dir = sys.argv[1]
input_ext = '.' + sys.argv[2]
output_name = sys.argv[3]

homedir = get_homedir()
framelist = get_framelist ( input_dir )

output_file = input_dir + '/' + output_name + '.out'
output = open(output_file, 'w')

print 'Reading tails of *' + input_ext + ' files in ' + input_dir + ' folder:'
for frame in framelist:
    filedir = homedir + '/' + str(frame)
    task = subprocess.Popen(['tail', '-1', frame ], stdout=subprocess.PIPE)
    data = task.stdout.read()
    print 'File: ' + filedir
    output.write(data)
#loop end

output.close()

print 'Done. Tails has been wrote in ' + output_file
print '--------------------------------------------------------------------------------'
print '--                Tails Reader V0.1 by Stephen Liu 20/09/2014                 --'
print '--                        stephenliu1989@gmail.com                            --'
print '--------------------------------------------------------------------------------'
