import json
import xmltodict
import os


class DataConverter:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.books_data = None

    def check_file_exists(self, file_path):
        if not os.path.isfile(file_path):
            print(f"指定されたファイルが見つかりません: {file_path}")
            return False
        print(f"ファイルを確認しました: {file_path}")
        return True

    def read_xml_file(self, xml_file_path):
        try:
            print(f"XMLファイルを読み込み中: {xml_file_path}")
            with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
                xml_content = xml_file.read()
            print("XMLファイルの読み込みが完了しました")
            return xml_content
        except FileNotFoundError:
            print(f"エラー: ファイルが見つかりません - {xml_file_path}")
            return None
        except Exception as e:
            print(f"ファイル読み込みエラー: {str(e)}")
            return None

    def parse_xml_to_dict(self, xml_content):
        try:
            print("XMLデータを解析中...")
            parsed_data = xmltodict.parse(xml_content)
            print("XMLデータの解析が完了しました")
            return parsed_data
        except Exception as e:
            print(f"XMLパーシングエラー: {str(e)}")
            return None

    def display_data_structure(self, data):
        if not data:
            print("表示するデータがありません")
            return
        
        print("\n=== データ構造の確認 ===")
        
        if 'books_catalog' in data:
            catalog = data['books_catalog']
            
            if 'store_info' in catalog:
                store_info = catalog['store_info']
                print(f"書店名: {store_info.get('store_name', '不明')}")
                print(f"所在地: {store_info.get('location', '不明')}")
                print(f"カタログ作成日: {store_info.get('catalog_date', '不明')}")
            
            if 'books' in catalog and 'book' in catalog['books']:
                books = catalog['books']['book']
                book_count = len(books) if isinstance(books, list) else 1
                print(f"登録書籍数: {book_count}冊")
                
                if isinstance(books, list) and books:
                    sample_book = books[0]
                    print(f"サンプル書籍: {sample_book.get('title', '不明')}")
                    print(f"著者: {sample_book.get('author', '不明')}")

    def create_output_folder(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            print(f"出力フォルダを作成しました: {self.output_folder}")
        else:
            print(f"出力フォルダが既に存在します: {self.output_folder}")

    def convert_dict_to_json(self, data):
        try:
            print("辞書データをJSON形式に変換中...")
            json_data = json.dumps(data, ensure_ascii=False, indent=4)
            print("JSON変換が完了しました")
            return json_data
        except Exception as e:
            print(f"JSON変換エラー: {str(e)}")
            return None

    def save_json_file(self, json_data, json_filename):
        json_file_path = os.path.join(self.output_folder, json_filename)
        
        try:
            print(f"JSONファイルを保存中: {json_file_path}")
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)
            print("JSONファイルの保存が完了しました")
            return True
        except Exception as e:
            print(f"ファイル保存エラー: {str(e)}")
            return False

    def check_file_size(self, file_path):
        try:
            file_size = os.path.getsize(file_path)
            if file_size > 1024:
                size_kb = file_size / 1024
                print(f"ファイルサイズ: {size_kb:.2f} KB")
            else:
                print(f"ファイルサイズ: {file_size} bytes")
            return file_size
        except Exception as e:
            print(f"ファイルサイズ取得エラー: {str(e)}")
            return 0

    def verify_conversion_result(self, json_filename):
        json_file_path = os.path.join(self.output_folder, json_filename)
        
        if not self.check_file_exists(json_file_path):
            return False
        
        try:
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                loaded_data = json.load(json_file)
            
            print("\n=== 変換結果の確認 ===")
            if 'books_catalog' in loaded_data:
                catalog = loaded_data['books_catalog']
                
                if 'store_info' in catalog:
                    store_info = catalog['store_info']
                    print(f"書店名: {store_info.get('store_name', '不明')}")
                
                if 'books' in catalog and 'book' in catalog['books']:
                    books = catalog['books']['book']
                    book_count = len(books) if isinstance(books, list) else 1
                    print(f"変換済み書籍数: {book_count}冊")
            
            return True
        except Exception as e:
            print(f"変換結果確認エラー: {str(e)}")
            return False

    def convert_xml_to_json(self, xml_filename, json_filename):
        xml_file_path = os.path.join(self.input_folder, xml_filename)
        
        if not self.check_file_exists(xml_file_path):
            return False
        
        xml_content = self.read_xml_file(xml_file_path)
        if xml_content is None:
            return False
        
        self.books_data = self.parse_xml_to_dict(xml_content)
        if self.books_data is None:
            return False
        
        # self.display_data_structure(self.books_data)
        
        self.create_output_folder()
        
        json_data = self.convert_dict_to_json(self.books_data)
        if json_data is None:
            return False
        
        success = self.save_json_file(json_data, json_filename)
        if success:
            json_file_path = os.path.join(self.output_folder, json_filename)
            self.check_file_size(json_file_path)
        
        return success


def main():
    print("=== 書店データ変換ツール ===")
    
    input_folder = "sample_data"
    output_folder = "converted_data"
    xml_filename = "books_catalog.xml"
    json_filename = "converted_books.json"
    
    converter = DataConverter(input_folder, output_folder)
    
    success = converter.convert_xml_to_json(xml_filename, json_filename)
    
    if success:
        print("\nXML→JSON変換が正常に完了しました")
        converter.verify_conversion_result(json_filename)
        # print("\nStep3の処理が正常に完了しました")
    else:
        print("\nXML→JSON変換中にエラーが発生しました")


if __name__ == "__main__":
    main()