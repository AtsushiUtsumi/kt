# -*- coding: utf-8 -*-

import json
import codecs
import util
import os
import re

import config
output_root = config.OUTPUT_ROOT

def mkdir(dir: str):
    if not os.path.isdir(dir):
        os.mkdir(dir)
    return

class CaseConverter:
    def __init__(self, word):
        self.word_list = list()
        word = re.sub('([A-Z])', '_\\1', word)
        if word[0] == '_':
            word = word[1:]
        if '_' in word:
            self.word_list = word.split('_')
        else:
            self.word_list.append(word.lower())
        # print(f'ローワースネークケース[{self.to_lower_snake_case()}]')
        # print(f'アッパースネークケース[{self.to_upper_snake_case()}]')
        # print(f'ローワーキャメルケース[{self.to_lower_camel_case()}]')
        # print(f'アッパーキャメルケース[{self.to_upper_camel_case()}]')
        # print(f'ケバブキャメルケース[{self.to_kebab_case()}]')
        pass
    def to_upper_snake_case(self):
        snake_case = '_'.join(self.word_list).upper()
        return snake_case
    def to_lower_snake_case(self):
        snake_case = '_'.join(self.word_list).lower()
        return snake_case
    def to_upper_camel_case(self):
        upper_camel_case_word = ''.join([i[0].upper() + i[1:] for i in self.word_list])
        return upper_camel_case_word
    def to_lower_camel_case(self):
        tmp = self.to_upper_camel_case()
        lower_camel_case_word = tmp[0].lower() + tmp[1:]
        return lower_camel_case_word
    def to_kebab_case(self):
        return self.to_lower_snake_case().replace('_', '-')


def application(extension: str):
    # 出力ディレクトリ設定
    dao_root = f'{output_root}/dao'
    mkdir(dao_root)
    template_root = f'{output_root}/template'
    mkdir(template_root)
    controller_root = f'{output_root}/controller'
    mkdir(controller_root)
    # 入力ファイル
    input_file_name = 'entity/entity.json'
    input_file = codecs.open(input_file_name, 'r', 'utf8')
    domain_dict = json.load(input_file)
    for table in domain_dict.get('entityList'):
        table_name = table['name']
        print("出力テーブル:" + table_name)
        entity_name = CaseConverter(table_name).to_upper_camel_case()
        screen_name = f"cdm04_02_{CaseConverter(table_name).to_lower_snake_case()}"
        page_name = CaseConverter(table_name).to_lower_camel_case()
        mkdir(dao_root + "/" + screen_name)
        mkdir(controller_root + "/" + screen_name)
        mkdir(template_root + "/" + screen_name)
        # DAO
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{dao_root}/{screen_name}/{entity_name}.{extension}')
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{dao_root}/{screen_name}/{entity_name}FindList.{extension}')
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{dao_root}/{screen_name}/{entity_name}Dao.{extension}')
        # Controller
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{controller_root}/{screen_name}/{entity_name}ListController.{extension}')
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{controller_root}/{screen_name}/{entity_name}ListForm.{extension}')
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{controller_root}/{screen_name}/{entity_name}DetailController.{extension}')
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{controller_root}/{screen_name}/{entity_name}DetailForm.{extension}')
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{controller_root}/{screen_name}/{entity_name}Bean.{extension}')
        # HTML
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{template_root}/{screen_name}/{page_name}List.html')
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', table, f'{template_root}/{screen_name}/{page_name}Detail.html')
    return