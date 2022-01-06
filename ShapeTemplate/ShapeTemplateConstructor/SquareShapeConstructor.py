import color.ColorService
from ShapeTemplate.ShapeTemplate import ShapeTemplate
from ShapeTemplate.Box import Box
from ShapeTemplate.Field import Field
from ShapeTemplate.Row import Row


def construct():
    first_rotate = Box([Row([Field(False), Field(True), Field(True), Field(False)]),
                        Row([Field(False), Field(True), Field(True), Field(False)]),
                        Row([Field(False), Field(False), Field(False), Field(False)]),
                        Row([Field(False), Field(False), Field(False), Field(False)])
                        ])

    second_rotate = Box([Row([Field(False), Field(True), Field(True), Field(False)]),
                         Row([Field(False), Field(True), Field(True), Field(False)]),
                         Row([Field(False), Field(False), Field(False), Field(False)]),
                         Row([Field(False), Field(False), Field(False), Field(False)])
                         ])

    third_rotate = Box([Row([Field(False), Field(True), Field(True), Field(False)]),
                        Row([Field(False), Field(True), Field(True), Field(False)]),
                        Row([Field(False), Field(False), Field(False), Field(False)]),
                        Row([Field(False), Field(False), Field(False), Field(False)])
                        ])

    fourth_rotate = Box([Row([Field(False), Field(True), Field(True), Field(False)]),
                         Row([Field(False), Field(True), Field(True), Field(False)]),
                         Row([Field(False), Field(False), Field(False), Field(False)]),
                         Row([Field(False), Field(False), Field(False), Field(False)])
                         ])

    return ShapeTemplate([first_rotate, second_rotate, third_rotate, fourth_rotate],
                         color.ColorService.get_yellow())
