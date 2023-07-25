# -*- coding: utf-8 -*-
import codecs
from jinja2 import Template
import os
import json

def get_template_file_path(language: str, template_type: str):
    template_file_path: str = ''
    template_file_path = f'./ore/{language}/{template_type}.{language}.j2'
    try:
        if os.path.isfile(template_file_path):
            return template_file_path
        else:
            print('テンプレートファイルが見つかりません')
            exit(0)
    except:
        print('テンプレートファイルが見つかりません')
        exit(0)

def create_concrete_from_params(template_file_name: str, params: dict, output_file_name: str):

    # テンプレートファイル読み込み
    if not os.path.isfile(template_file_name):
        print('テンプレートファイル[' + template_file_name + ']が見つかりませんでした')
        return
    template_file = codecs.open(template_file_name, 'r', 'utf8')
    template = Template(template_file.read())
    template_file.close()

    # 出力ファイル書き込み
    try:
        output_file = codecs.open(output_file_name, 'w', 'utf8')
        output_file.write(template.render(params))
        output_file.close()
        print('[' + output_file_name + ']を作成しました')
    except:
        print('ファイル[' + output_file_name + ']を作成できませんでした')
        pass
    return

def create_concrete_from_files(template_file_name: str, params_file_name: str, output_file_name: str):

    # テンプレートファイル読み込み
    if not os.path.isfile(template_file_name):
        print('テンプレートファイル[' + template_file_name + ']が見つかりませんでした')
        return
    template_file = codecs.open(template_file_name, 'r', 'utf8')
    template = Template(template_file.read())
    template_file.close()

    # パラメータファイル読み込み
    if not os.path.isfile(params_file_name):
        print('パラメータファイル[' + params_file_name + ']が見つかりませんでした')
        return
    params_file = codecs.open(params_file_name, 'r', 'utf8')
    params = json.load(params_file)
    params_file.close()

    # 出力ファイル書き込み
    try:
        output_file = codecs.open(output_file_name, 'w', 'utf8')
        output_file.write(template.render(params))
        output_file.close()
        print('ファイル[' + output_file_name + ']を作成しました')
    except:
        print('ファイル[' + output_file_name + ']を作成できませんでした')
        pass
    return