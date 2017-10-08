#! /usr/bin/tcsh
#while ( 1 )
#  if ( ! -f ~/pynq_home_mount//wav_copied.txt ) then
#    arecord -D hw:0,0 -r 48 -f S16_LE --channels 2 test.wav -d 2;
#    mv test.wav ~/pynq_home_mount//;
#    echo "1" > ~/pynq_home_mount//wav_copied.txt;
#  endif
#  usleep 1;
#end
while ( 1 )
  if ( ! -f ~/pynq_home_mount/wav_copied.txt ) then
    arecord -D hw:0,0 -r 48 -f S16_LE --channels 2 test.wav -d 2;
    mv test.wav ~/pynq_home_mount/;
    echo "1" > ~/pynq_home_mount/wav_copied.txt;
  endif
  usleep 1;
end
