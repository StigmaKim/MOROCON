from google.appengine.api import images

class ImgHandler():
    def transform(self, file):
        img = images.Image(file)
        img.im_feeling_lucky()
        img.resize(600, 600)
        png_data = img.execute_transforms(output_encoding=images.PNG)
        
        return png_data