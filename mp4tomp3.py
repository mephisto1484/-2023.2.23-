from moviepy.editor import *
import argparse
def outputmp3(input_path, output_path):
    listdir = os.listdir(input_path)   # 获得路径所有文件名
    mp4namelist = [name for name in listdir if name.endswith('.mp4')]   # 筛选出所有MP4
 
    for file in mp4namelist:
        filepath = os.path.join(input_path, file)  # mp4文件路径
        video = VideoFileClip(filepath)
 
        # 构造mp3文件名
        file_list = list(file)
        file_list[-1] = '3'
        file_name_mp3 = ''.join(file_list)
 
        out_listdir = []
        out_filepath = ''
        if len(output_path) == 0:
            # 输出MP3文件到默认路径
            out_listdir = listdir
            out_filepath = os.path.join(input_path, file_name_mp3)
        else:
            # 输出MP3文件到指定路径
            out_listdir = os.listdir(output_path)
            out_filepath = os.path.join(output_path, file_name_mp3)
 
        # 检查文件是否已经存在
        if file_name_mp3 in out_listdir:
            continue
        audio = video.audio
        audio.write_audiofile(out_filepath)
 
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default='./')
    parser.add_argument('-o', '--output', type=str, default='./')
    args = parser.parse_args()
    input_path = args.input # 绝对地址
    output_path = args.output # 不传输出路径则默认生成在input_path下
    outputmp3(input_path, output_path)