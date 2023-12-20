import pytest
from funcs_module import main

def test_main():
    pdf_path = "/home/mjoudy/Documents/codes/psiori/pdf_parsing/li.pdf"  # Replace with the actual path to a sample PDF file
    expected_output = [
        {
            'title': 'Chapter 1',
            'pages': '1-5',
            'text': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.'],
            'images': [['image_1_1.png', 'image_1_2.png']]
        },
        {
            'title': 'Chapter 2',
            'pages': '6-10',
            'text': ['Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.', 'Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur.'],
            'images': [['image_2_1.png', 'image_2_2.png', 'image_2_3.png']]
        }
    ]  # Replace with the expected output for the sample PDF file
    
    assert main(pdf_path) == expected_output