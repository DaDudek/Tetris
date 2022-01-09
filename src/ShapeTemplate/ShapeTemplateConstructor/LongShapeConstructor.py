import src.color.ColorService
from src.ShapeTemplate.ShapeTemplate import ShapeTemplate
from src.ShapeTemplate.Box import Box
from src.ShapeTemplate.Field import Field
from src.ShapeTemplate.Row import Row


def construct() -> ShapeTemplate:
    first_rotate = Box([Row([Field(False), Field(False), Field(False), Field(False)]),
                        Row([Field(True), Field(True), Field(True), Field(True)]),
                        Row([Field(False), Field(False), Field(False), Field(False)]),
                        Row([Field(False), Field(False), Field(False), Field(False)])
                        ])

    second_rotate = Box([Row([Field(False), Field(False), Field(True), Field(False)]),
                         Row([Field(False), Field(False), Field(True), Field(False)]),
                         Row([Field(False), Field(False), Field(True), Field(False)]),
                         Row([Field(False), Field(False), Field(True), Field(False)])
                         ])

    third_rotate = Box([Row([Field(False), Field(False), Field(False), Field(False)]),
                        Row([Field(False), Field(False), Field(False), Field(False)]),
                        Row([Field(True), Field(True), Field(True), Field(True)]),
                        Row([Field(False), Field(False), Field(False), Field(False)])
                        ])

    fourth_rotate = Box([Row([Field(False), Field(True), Field(False), Field(False)]),
                         Row([Field(False), Field(True), Field(False), Field(False)]),
                         Row([Field(False), Field(True), Field(False), Field(False)]),
                         Row([Field(False), Field(True), Field(False), Field(False)])
                         ])

    return ShapeTemplate([first_rotate, second_rotate, third_rotate, fourth_rotate],
                         src.color.ColorService.get_maritime())
