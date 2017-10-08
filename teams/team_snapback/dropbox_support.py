import dropbox, sys, os
import config

dbx = dropbox.Dropbox(config.dropbox_key)
project_dir = '/home/xilinx/jupyter_notebooks/nhan_dev/snapback1/capture_moments'
print('Attempting to upload...')

if not os.path.exists(project_dir):
	project_dir = raw_input("Can't find videos. Enter the path of the snapback directory! ") 
counter = 0
for dir, dirs, files in os.walk(project_dir):
	for file in files:
		try:
			file_path = os.path.join(dir,file)
			dest_path = os.path.join('/SnapBack',file)
			print('Uploading {} to {}'.format(file_path, dest_path))
			with open(file_path, 'rb') as f:
				dbx.files_upload(f.read(), dest_path, mute = True)
		except Exception as err:
			print("Failed to upload {}\n{}".format(file, err))
			counter += 1

print("Finished with {} errors".format(counter))

