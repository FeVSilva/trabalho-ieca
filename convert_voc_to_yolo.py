import os
import xml.etree.ElementTree as ET

def convert_voc_to_yolo(voc_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for xml_file in os.listdir(voc_dir):
        if not xml_file.endswith('.xml'):
            continue
        
        xml_path = os.path.join(voc_dir, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        image_width = int(root.find('size/width').text)
        image_height = int(root.find('size/height').text)
        
        output_path = os.path.join(output_dir, os.path.splitext(xml_file)[0] + '.txt')
        
        with open(output_path, 'w') as output_file:
            for obj in root.findall('object'):
                class_name = obj.find('name').text
                class_id = classes.index(class_name)
                
                bndbox = obj.find('bndbox')
                xmin = float(bndbox.find('xmin').text)
                ymin = float(bndbox.find('ymin').text)
                xmax = float(bndbox.find('xmax').text)
                ymax = float(bndbox.find('ymax').text)
                
                x_center = (xmin + xmax) / 2.0 / image_width
                y_center = (ymin + ymax) / 2.0 / image_height
                box_width = (xmax - xmin) / image_width
                box_height = (ymax - ymin) / image_height
                
                output_file.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")

classes = [ 'tree','red_light','green_light','crosswalk','blind_road','sign', 'person', 'bicycle', 'bus', 'truck', 'car','motorcycle', 'reflective_cone', 'ashcan', 'warning_column','roadblock', 'pole', 'dog', 'tricycle','fire_hydrant' ]

voc_annotations_dir = r'C:\Users\FERNANDO\Downloads\WOTR\Annotations'
yolo_output_dir = r'C:\Users\FERNANDO\Downloads\WOTR\Output'

convert_voc_to_yolo(voc_annotations_dir, yolo_output_dir)
