import pathlib
import requests
import urllib.parse as url_parser
import os

def download_files(url: str, save_dest: str):
    url = url_parser.urlparse(url)
    save_dest = pathlib.Path(save_dest)
    terminal_sz = os.get_terminal_size().columns
    image_path_split: list[str] = url.path[1:].rsplit('.', 1)
    image_path_split.append(image_path_split[1])

    image_idx = 0
    power = 1
    pow_cnt = 0
    for ch in image_path_split[0][::-1]:
        try:
            power = power * 10 ** pow_cnt
            image_idx = image_idx + int(ch) * power
            pow_cnt += 1
        except ValueError:
            break

    image_path_split[0] = image_path_split[0][0:-pow_cnt]
    save_dest.mkdir(exist_ok=True)
    retry = 5
    while retry:
        image_path_split[1] = f'{image_idx:0{pow_cnt}d}'
        image_str = image_path_split[0] + image_path_split[1] + '.' + image_path_split[2]
        url = url._replace(path=image_str)
        msg = f'Downloading {url.geturl()} '
        msg_sz = len(msg) + 1
        print(msg, end='')
        response = requests.get(url.geturl())
        if response.status_code != 200:
            msg = f' [Download Failed]'
            dots = '.' * (terminal_sz - msg_sz - len(msg))
            print(dots + msg)
            retry -= 1
        elif response.status_code == 200:
            with open(save_dest / image_str, 'wb') as fhandle:
                msg = f' [Saving {save_dest / image_str}]'
                dots = '.' * (terminal_sz - msg_sz - len(msg))
                print(dots + msg)
                fhandle.write(response.content)
        image_idx += 1


if __name__ == '__main__':
    download_files('http://699340.youcanlearnit.net/image001.jpg', './images/')
