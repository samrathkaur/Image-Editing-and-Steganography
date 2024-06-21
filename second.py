import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io

# Set the title of the app
st.title('Basic Image Editor')

# Upload an image
st.subheader("Input")
input_mode = st.radio("Input mode", ["Camera", "File upload"])

uploaded_file = None
if input_mode == "Camera":
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        uploaded_file = img_file_buffer.getvalue()
else:
    file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])
    if file is not None:
        uploaded_file = file.getvalue()

if uploaded_file is None:
    st.stop()

# If an image is uploaded
if uploaded_file is not None:
    # Open the image
    image = Image.open(io.BytesIO(uploaded_file))
    
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Use the sliders and options below to edit the image.")
    
    # Image editing options
    # Brightness
    brightness = st.slider('Brightness', 0.1, 3.0, 1.0)
    enhancer = ImageEnhance.Brightness(image)
    img_output = enhancer.enhance(brightness)
    
    # Contrast
    contrast = st.slider('Contrast', 0.1, 3.0, 1.0)
    enhancer = ImageEnhance.Contrast(img_output)
    img_output = enhancer.enhance(contrast)
    
    # Sharpness
    sharpness = st.slider('Sharpness', 0.1, 3.0, 1.0)
    enhancer = ImageEnhance.Sharpness(img_output)
    img_output = enhancer.enhance(sharpness)
    
    # Apply a filter
    filter_option = st.selectbox('Filter', ['None', 'BLUR', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'SHARPEN'])
    if filter_option == 'BLUR':
        img_output = img_output.filter(ImageFilter.BLUR)
    elif filter_option == 'CONTOUR':
        img_output = img_output.filter(ImageFilter.CONTOUR)
    elif filter_option == 'DETAIL':
        img_output = img_output.filter(ImageFilter.DETAIL)
    elif filter_option == 'EDGE_ENHANCE':
        img_output = img_output.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_option == 'EDGE_ENHANCE_MORE':
        img_output = img_output.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter_option == 'EMBOSS':
        img_output = img_output.filter(ImageFilter.EMBOSS)
    elif filter_option == 'SHARPEN':
        img_output = img_output.filter(ImageFilter.SHARPEN)
    
    # Display the edited image
    st.image(img_output, caption='Edited Image.', use_column_width=True)
    
    # Option to download the edited image
    img_output = img_output.convert("RGB")
    buf = io.BytesIO()
    img_output.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="Download edited image",
        data=byte_im,
        file_name="edited_image.jpg",
        mime="image/jpeg"
    )
