# -*- coding: utf-8 -*-
import base64


def pic2str(file, functionName):
    pic = open(file, 'rb')
    content = '{} = {}\n'.format(functionName, base64.b64encode(pic.read()))
    pic.close()

    with open('img2byte.py', 'a') as f:
        f.write(content)


if __name__ == '__main__':
    pic2str('images/close.png', 'close')
    pic2str('images/contact.png', 'contact')
    pic2str('images/delete.png', 'delete')
    pic2str('images/device.png', 'device')
    pic2str('images/Female.png', 'Female')
    pic2str('images/gender.png', 'gender')
    pic2str('images/icon.png', 'iconimg')
    pic2str('images/logout.png', 'logot')
    pic2str('images/Male.png', 'Male')
    pic2str('images/org.png', 'org')
    pic2str('images/router.png', 'router')
    pic2str('images/Switch.png', 'Switch')
    pic2str('images/time.png', 'time')
    pic2str('images/setting.png', 'setting')
    pic2str('images/toggle-right.png', 'ssh_img')
    pic2str('images/toggle-left.png', 'telnet_img')