# IdolGAN ~~[adoːkẽꜜɴ]~~

We use [HiFaceGAN](https://github.com/Lotayou/Face-Renovation) and [KID-F Dataset](https://github.com/PCEO-AI-CLUB/KID-F).

# Usage
### Environment
- Ubuntu/CentOS
- PyTorch 1.0+
- CUDA 10.1
- python packages: opencv-python, tqdm, 
- Data augmentation tool: [imgaug](https://imgaug.readthedocs.io/en/latest/source/installation.html#installation-in-pip)
- [Face Recognition Toolkit](https://github.com/ageitgey/face_recognition) for evaluation
- [tqdm](https://github.com/tqdm/tqdm) to make you less anxious when testing:)

### Checkpoint
We provide Model Checkpoint which trained from KID-F Dataset. We used train_dataset of KID-F for training, which takes 2 days on a GTX 1080 Ti. We upload the checkpoint on our [googledrive](https://drive.google.com/drive/folders/1GrZIofQc3uWFVWserxgPEO97DZEJYOuK?usp=sharing).

### Configurations
The configurations is stored in `options/config_hifacegan.py`, the options should be self-explanatory, but feel free to leave an issue anytime.

### Training and Testing
```
python train.py            # A fool-proof training script
python test.py             # Test on synthetic dataset
python test_nogt.py        # Test on real-world images
python two_source_test.py  # Visualization of Fig 5
```
### Evaluation
We used PSNR, SSIM, FID, LPIPS, IDD.
Coming Soon!

### Benchmark

We use HiFaceGAN model. 
We compared HiFaceGAN's performance about 300 K-pop Idol images with 5 Metrices(PSNR, SSIM, FID, LPIPS, IDD).
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

### License
Don't do what you think. anything
