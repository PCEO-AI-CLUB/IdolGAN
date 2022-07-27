# IdolGAN ~~[adoːkẽꜜɴ]~~

IdolGAN project is inspired by our pure passion which is Super-resolution of our favorite Idols. So We google about it. But many SR models can't generate an image we are satisfied with. We think models trained by FFHQ and Celeb-A never Super-resolution our favorite Idols, Therefore, we gather many high-quality K-pop Idol images from the internet. In our First step, Face is very important in our purpose. so we collect about 6000 K-pop girl group images(at least 512*512 size, even the face alone! but resized to 512*512 size). In this repo, we propose our first step fat pops and wrinkled old woman in FFHQ, Celeb-A or etc can't generate our idol. just see it. this repo or our next step whatever. LOL
We used [HiFaceGAN](https://github.com/Lotayou/Face-Renovation) and [KID-F Dataset](https://github.com/PCEO-AI-CLUB/KID-F).

# Usage
### Environment
- Ubuntu
- PyTorch 1.0+
- CUDA 10.1
- python packages: opencv-python, tqdm, 
- Data augmentation tool: [imgaug](https://imgaug.readthedocs.io/en/latest/source/installation.html#installation-in-pip)
- [Face Recognition Toolkit](https://github.com/ageitgey/face_recognition) for evaluation
- [tqdm](https://github.com/tqdm/tqdm) to make you less anxious when testing:)
- cv2 

for crop.py(view code, edit yourself)
  cv2, mediapipe, tqdm  

for degrad.py(view code, edit yourself)
  cv2, tqdm
  
### Checkpoint
We provide Model Checkpoint which trained from KID-F Dataset. We used train_dataset of KID-F for training, which takes 2 days on a GTX 1080 Ti. We upload the checkpoint on our [Google Drive](https://drive.google.com/drive/folders/1GrZIofQc3uWFVWserxgPEO97DZEJYOuK?usp=sharing).

### Configurations
The configurations is stored in `options/config_hifacegan.py`, the options should be self-explanatory, but feel free to leave an issue anytime.

### Evaluation
We used PSNR, SSIM, FID, LPIPS, IDD.
Coming Soon!

### Benchmark

We use HiFaceGAN model. 
We compared HiFaceGAN's performance of about 300 K-pop Idol images with 5 Metrics(PSNR, SSIM, FID, LPIPS, IDD).
Column FFHQ is metrices calculated from Pretrained Models(HiFaceGAN) with FFHQ Downloaded from [HiFaceGAN](https://github.com/Lotayou/Face-Renovation).
Column Idol Dataset (Ours) calculated from HiFaceGAN trained with KID-F.
In our work, for training, degrading code follow HiFaceGAN's method.

The Metrices is calculated from 300 K-pop Idol 512*512 face images inference of each model and original images. 

|            |       FFHQ     |     Idol Dataset (Ours)    |
|:----------:|:--------------:|:--------------------------:|
|      PSNR↑ |      31.82     |            32.49           |
|      SSIM↑ |       0.72     |            0.758           |
|     LPIPS↓ |      0.151     |            0.109           |
|      FID↓  |      0.574     |            0.159           |
|      IDD↓  |     0.00637    |           0.00496          |

# Citation
```
@notyet{
  title = {},
  author = {Dongkyu Kim, Donggeon Han, Hyunwook Kwon, Dain Jeong, Cheol H. Jeong},
  month = {August},
  year = {2022}
}
```
