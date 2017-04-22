import os, sys

def call():
    # cmd1 = "echo yes"
    # os.system(cmd1)

    # cmd2 = "ffmpeg -version"
    # os.system(cmd2)

    # filename = sys.argv[1]
    # print(filename)
    # cmd3 = "echo {name}.mp4 ".format(name = filename)
    # os.system(cmd3)

    timejpg = "00:00:04"

    filename = sys.argv[1]
    array = filename.split('.')
    mainname = array[0]

    if sys.argv[2]:
        timejpg = " "+sys.argv[2]
        print "time for snapshot jpg is {timejpg}"

    print(filename, mainname)
    cmd4 = "ffmpeg -i {name} -profile:v baseline -level 3.0  -acodec aac -strict -2 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls {main}.m3u8".format(name = filename, main = mainname)
    cmd5 = "time ffmpeg -ss {timecut} -i {name} -f image2 -y {picture}.jpg".format(timecut = timejpg, name = filename, picture = mainname)
    # cmd5 = "time ffmpeg -ss 00:00:49 -i {name} -f image2 -y {picture}.jpg".format(name = filename, picture = mainname)

    os.system(cmd5)
    os.system(cmd4)

# call()


if  __name__ == '__main__':
    call()

