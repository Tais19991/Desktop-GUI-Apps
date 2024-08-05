
class ImgSizeChanger:
    def __init__(self, image: object):
        self.img = image

    def update(self, subject):
        print(f"SizeChanger: update called with gain {subject.gain}")
        self.img.resize_img(subject.gain)
        self.img.update_multi_img_canvas()


class ImgRotator:
    def __init__(self, image: object):
        self.img = image

    def update(self, subject):
        print(f"ImgRotator: update called with angle -  {subject.gain}")
        self.img.rotate_img(subject.gain)
        self.img.update_multi_img_canvas()


class ImgOpacityModifier:
    def __init__(self, image: object):
        self.img = image

    def update(self, subject):
        print(f"Opacity: update called with opacity {subject.gain}")
        self.img.change_img_opacity(subject.gain)
        self.img.update_multi_img_canvas()


class ImgSpacer:
    def __init__(self, image: object):
        self.img = image

    def update(self, subject):
        print(f"Change space: update called with space {subject.gain}")
        self.img.update_multi_img_canvas(subject.gain)
