

import os
import json

input_dir = "/Users/llp/Movies/input"
output_dir = "/Users/llp/Movies/output"

movies = [os.path.join(input_dir, file) for file in os.listdir(
    input_dir) if os.path.isdir(os.path.join(input_dir, file))]
# print(movies)

for movie in movies:
    ep_list = [os.path.join(movie, ep) for ep in os.listdir(
        movie) if os.path.isdir(os.path.join(movie, ep))]
    # print(ep_list)

    for ep in ep_list:

        entry_file = os.path.join(ep, "entry.json")
        # print( os.path.exists(entry_file) )
        with open(entry_file, encoding="utf-8", ) as fp:

            info = json.load(fp)

            # 建立视频合集 的 文件夹:
            output_movie_path = os.path.join(output_dir, info["title"])

            if os.path.exists(output_movie_path) == False:
                # print(output_movie_path)
                os.mkdir(output_movie_path)

            # 普通视频 字段 叫做 page_data   
            if "page_data" in info:
                # print(info["page_data"])
                # 视频分集 的 文件夹:
                if "part" in info["page_data"]:
                    video_name =  str(info["page_data"]["page"]) + " " +   info["page_data"]["part"] + "1.mp4"
                else:  # 只有一集
                    # print(output_movie_path)
                    video_name = info["title"] + "1.mp4"
            # 影视视频字段叫做ep
            elif "ep" in info:
                video_name =  str(info["ep"]["page"]) + " " + info["ep"]["index_title"] + "1.mp4"
            else:
                raise ("还有别的类型")
            
            output_file_abs_path = os.path.join(
            output_movie_path, video_name)

            video_m4s_path = os.path.join(
                ep, info["type_tag"], "video.m4s")
            audio_m4s_path = os.path.join(
                ep, info["type_tag"], "audio.m4s")

            if os.path.exists(video_m4s_path) and os.path.exists(audio_m4s_path):
                # 有3个路径,前2个路径都是数字组成的, 最后的路径文件名有中文等符号,为了消除空格的影响,把输出路径用双引号包起来.
                cmd = "ffmpeg -i " + video_m4s_path + " -i " + audio_m4s_path + \
                    " -vcodec copy -acodec copy " + "\"" + output_file_abs_path + "\""
                print(cmd)
            else:  # 文件不存在
                raise ("文件不存在")
            os.system(cmd)