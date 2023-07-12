from tools.set_type import set_type
from tools.set_path import set_path
from tools.set_link import set_link
from tools.download_video import download

download_type = int(set_type())

match download_type:
    case 1:
        download(set_link(), set_path(), download_type)
        print("\nArquivo baixado com sucesso!")

    case 2:
        download(set_link(), set_path(), download_type)
        print("\nArquivo baixado com sucesso!")

    case _:
        print("\nVocê digitou uma opção inválida")
