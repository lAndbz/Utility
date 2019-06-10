import os
import sys
import string
import zipfile

def del_punc(word):
    """删除单词后标点
    
    [description]
    
    Arguments:
        word {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    trantab = str.maketrans({key: None for key in string.punctuation})

    return word.translate(trantab) 

def walk_path(target_path):
    for folderName, subfolders, filenames in os.walk(target_path):
        print('The current folder is ' + folderName)
        
        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
        
        print('')


def backup2zip(folder):
    '''Backup the entire contents of "folder" into a ZIP file.
    
    [description]
    
    Arguments:
        folder {[type]} -- [description]
    '''
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # TODO: Create the ZIP file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        #Add all the files in this folder to the ZIP file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder)) and filename.endswith('.zip'):
                continue # don't backup the ZIP file.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python utility path')
        sys.exit()
    # walk_path(sys.argv[1])
    backup2zip(sys.argv[1])    

