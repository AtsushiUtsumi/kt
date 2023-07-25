# -*- coding: utf-8 -*-

import json
import codecs
import util
import os

import config
output_root = config.OUTPUT_ROOT

print('出力ディレクトリ = ' + str(output_root))

def mkdir(dir: str):
    if not os.path.isdir(dir):
        os.mkdir(dir)
    return

def test():
    domain_file_name = 'entity/entity.json'
    domain_file = codecs.open(domain_file_name, 'r', 'utf8')
    domain_dict = json.load(domain_file)
    for entity in domain_dict.get('entityList'):
        entity_name = entity['name']

        # ドメイン層の出力ルートディレクトリ作成
        # value_object_root = f'../src/lib'
        # value_object_output_dir = f'{value_object_root}/{entity_name}'
        # if not os.path.isdir(value_object_output_dir):
        #     os.mkdir(value_object_output_dir)
        entity_root = f'../src/lib/server'
        entity_output_dir = f'{entity_root}/{entity_name}'
        mkdir(entity_output_dir)
        # プレゼンテーション層(今はひとまずsvelte、e2eはplaywright)
        mkdir(f'../src/routes/{entity_name}')
        if not os.path.isdir(f'../tests/{entity_name}'):
            os.mkdir(f'../tests/{entity_name}')
        if not os.path.isdir(f'../src/routes/api/{entity_name}'):
            os.mkdir(f'../src/routes/api/{entity_name}')
        util.create_concrete_from_params('presentation/+server.ts.j2', entity, f'../src/routes/api/{entity_name}/+server.ts')
        util.create_concrete_from_params('presentation/+page.server.ts.j2', entity, f'../src/routes/{entity_name}/+page.server.ts')
        util.create_concrete_from_params('presentation/+page.svelte.j2', entity, f'../src/routes/{entity_name}/+page.svelte')
        util.create_concrete_from_params('presentation/test.ts.j2', entity, f'../tests/{entity_name}/{entity_name}.test.ts')

        # ドメイン層の出力ルートディレクトリ作成
        # value_object_root = f'../src/lib'
        # value_object_output_dir = f'{value_object_root}/{entity_name}'
        # if not os.path.isdir(value_object_output_dir):
        #     os.mkdir(value_object_output_dir)
        entity_root = f'../src/lib/server'
        entity_output_dir = f'{entity_root}/{entity_name}'
        if not os.path.isdir(entity_output_dir):
            os.mkdir(entity_output_dir)
        # エンティティ
        util.create_concrete_from_params('entity/entity.ts.j2', entity, f'{entity_output_dir}/{entity_name}.ts')
        util.create_concrete_from_params('entity/entity.test.ts.j2', entity, f'{entity_output_dir}/{entity_name}.test.ts')

        # アプリケーション層の出力ルートディレクトリ作成
        presentation_root = f'../src/lib/server'
        presentation_output_dir = f'{presentation_root}/{entity_name}'
        if not os.path.isdir(presentation_output_dir):
            os.mkdir(presentation_output_dir)
        # アプリケーション層とそのテストコード
        util.create_concrete_from_params('entity/presentationService.ts.j2', entity, f'{presentation_output_dir}/{entity_name}presentationService.ts')
        util.create_concrete_from_params('entity/presentationService.test.ts.j2', entity, f'{presentation_output_dir}/{entity_name}presentationService.test.ts')
    return

# エンティティのイコールは識別子が一致していることであり、
# 値オブジェクトのイコールは全てのメンバが一致しているってことかな?

# プレゼンテーション層より外側(フレームワークに依存する所など)を作成する。
# 拡張子が指定できるのはseleniumなど言語が複数選べる場合を考慮してはいるがたいていは指定する必要が内容にしておく。
def presentation(framework: str, extension: str):
    print('プレゼンテーション層の出力を行います')
    domain_root = f'{output_root}/Domain'
    mkdir(domain_root)
    value_object_root = f'{domain_root}/ValueObject'
    mkdir(value_object_root)
    # 画面毎に出力しないといけないのでWebアプリの場合はURLリストみたいな感じ
    presentation_root = f'{output_root}/presentation'
    mkdir(presentation_root)
    domain_file_name = 'entity/entity.json'
    domain_file = codecs.open(domain_file_name, 'r', 'utf8')
    domain_dict = json.load(domain_file)
    for entity in domain_dict.get('entityList'):
        domain_name = entity['name']
        # アプリケーション層
        presentation_output_dir = f'{presentation_root}/{domain_name}'
        mkdir(presentation_output_dir)
        util.create_concrete_from_params(f'entity/{extension}/presentationService.{extension}.j2', entity, f'{presentation_output_dir}/{domain_name}presentationService.{extension}')
    return