from flask import send_file


def get_img(img_id):
    # 生成 WebP 图片
    # 这里假设你已经使用 Pillow 或其他库将图像保存为 WebP 格式
    webp_image_path = f'source/img/{img_id}'

    # 返回 WebP 图片
    return send_file(webp_image_path, mimetype='image/webp', as_attachment=True, download_name='image.webp')
