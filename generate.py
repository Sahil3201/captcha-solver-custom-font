#!/usr/bin/env python3

import os
import numpy
import random
import string
import cv2
import argparse
import captcha.image
import csv
import glob
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-file', help='Name of output file', type=str)
    parser.add_argument('--count', help='How many captchas to generate', type=int)
    parser.add_argument('--output-dir', help='Where to store the generated captchas', type=str)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    parser.add_argument('--fontfile', help='File with the font to use in captchas', type=str)
    args = parser.parse_args()

    if args.output_file is None:
        print("Please specify the output file name")
        exit(1)

    if args.count is None:
        print("Please specify the captcha count to generate")
        exit(1)

    if args.output_dir is None:
        print("Please specify the captcha output directory")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)
    
    if args.fontfile is None:
        print("Please specify the fonts file")
        exit(1)

    captcha_paths = glob.glob(os.path.join(args.output_dir, "*"))
    for path in captcha_paths:
        os.remove(path)

    captcha_generator = captcha.image.ImageCaptcha(width=128, height=64, fonts=[args.fontfile])
    data = []

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    symbols_file.close()

    print("Generating "+str(args.count)+" captchas with symbol set {" + captcha_symbols + "}")

    if not os.path.exists(args.output_dir):
        print("Creating output directory " + args.output_dir)
        os.makedirs(args.output_dir)

    start = time.time()
    for i in range(args.count):
        random_str = ''.join(random.sample(captcha_symbols, random.randint(1, 6)))
        image_path = os.path.join(args.output_dir, "%06d"%(i,)+'.png')
        data.append([random_str,"%06d"%(i,)+'.png'])
        # if os.path.exists(image_path):
        #     version = 1
        #     while os.path.exists(os.path.join(args.output_dir, random_str + '_' + str(version) + '.png')):
        #         version += 1
        #     image_path = os.path.join(args.output_dir, random_str + '_' + str(version) + '.png')

        image = numpy.array(captcha_generator.generate_image(random_str))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
        cv2.imwrite(image_path, image)
        if (i+1) % 1000 == 0:
            print("Generating..{} - {} % done   \r".format(i,round((i+1)/args.count * 100.0, 2)), end="")

    numpy.savetxt(args.output_file,data,delimiter =",",fmt ='% s')
    print("Generation complete in (sec): "+str(time.time()-start))

if __name__ == '__main__':
    main()
