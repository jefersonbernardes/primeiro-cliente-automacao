from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import random


class PrimeiroCliente:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_experimental_option("prefs", {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "profile.default_content_settings.popups": 0,
        })
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException,
                                ElementNotVisibleException,
                                ElementNotSelectableException]
        )
        self.linkSite = 'https://cursoautomacao.netlify.app'
        self.opcao_radio_button = ''
        self.opcao_pais_dropdown = ''
        self.cidades_cadastradas = []

    def Iniciar(self):
        self.validarRadioButton()
        self.validarDropdown()
        self.acessarSite()
        self.selecionarRadioButton()
        self.selecionarDropdown()
        self.selecionarCidades()
        self.realizarDownloads()
        self.acessarNivelAcesso()
        self.rodarNovamente()

    def validarRadioButton(self):
        self.opcao_radio_button = input(
            'Qual opção deseja selecionar em "Exemplo Radio Buttons"? (Windows10/Mac/Linux) ').lower()
        if self.opcao_radio_button not in ('windows10', 'mac', 'linux'):
            print(
                'Campo obrigatório. Favor escolher uma opção entre Windows10/Mac/Linux')
            self.validarRadioButton()

    def validarDropdown(self):
        self.opcao_pais_dropdown = input(
            'Qual país deseja selecionar? (Brasil/Estados Unidos/Canada) ').lower()
        if self.opcao_pais_dropdown not in ('brasil', 'estados unidos', 'canada'):
            print(
                'Campo obrigatório. Favor escolher uma opção entre Brasil/Estados Unidos/Canada')
            self.validarDropdown()

    def acessarSite(self):
        self.driver.get(self.linkSite)

    def selecionarRadioButton(self):
        windows_radio_button = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//input[@value="windows 10"]')))
        mac_radio_button = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//input[@value="Mac"]')))
        linux_radio_button = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//input[@value="Linux"]')))
        if self.opcao_radio_button == 'windows10':
            windows_radio_button.click()
        if self.opcao_radio_button == 'mac':
            mac_radio_button.click()
        if self.opcao_radio_button == 'linux':
            linux_radio_button.click()

    def selecionarDropdown(self):
        lista_pais_dropdown = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//select[@id="paisselect"]')))
        opcao = Select(lista_pais_dropdown)
        if self.opcao_pais_dropdown == 'brasil':
            opcao.select_by_index(0)
        if self.opcao_pais_dropdown == 'estados unidos':
            opcao.select_by_index(1)
        if self.opcao_pais_dropdown == 'canada':
            opcao.select_by_index(2)

    def selecionarCidades(self):
        cidades = self.wait.until(expected_conditions.visibility_of_all_elements_located(
            (By.XPATH, '//table[@class="table table-striped"]/tbody//tr//td')))
        for cidade in cidades:
            self.cidades_cadastradas.append(cidade.text)
        print(self.cidades_cadastradas)

    def realizarDownloads(self):
        download_excel = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[@href="https://drive.google.com/uc?export=download&id=16p2lbFveNc8N8KNP9TH9FQs0psaSPVf7"]')))
        download_pdf = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[@href="https://drive.google.com/uc?export=download&id=1SE4Dvkc5TBRxDQnfkdqulbBxhpqYqlBx"]')))
        download_docx = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[@href="https://drive.google.com/uc?export=download&id=1uKoV4pmyhDAgXwLyKlb5qPLJE9I0OUL1"]')))
        download_texto = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[@href="https://drive.google.com/uc?export=download&id=1Dq-6XC8K0QRXdmNYyHvJhYH2cq29Svjv"]')))
        download_csv = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[@href="https://drive.google.com/uc?export=download&id=11r_wdoaX8_5gxr6y83gEf56GDG70sFW_"]')))
        self.driver.execute_script('arguments[0].click()', download_excel)
        time.sleep(5)
        self.driver.execute_script('arguments[0].click()', download_pdf)
        time.sleep(5)
        self.driver.execute_script('arguments[0].click()', download_docx)
        time.sleep(5)
        self.driver.execute_script('arguments[0].click()', download_texto)
        time.sleep(5)
        self.driver.execute_script('arguments[0].click()', download_csv)

    def acessarNivelAcesso(self):
        acesso1 = self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//label[@for="acessoNivel1Checkbox"]')))
        acesso2 = self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//label[@for="acessoNivel2Checkbox"]')))
        acesso3 = self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//label[@for="acessoNivel3Checkbox"]')))
        print(
            f'Os acessos disponíves são: {acesso1.text}, {acesso2.text} e {acesso3.text}.')

    def rodarNovamente(self):
        rodar_novamente = input(
            'Deseja rodar o programa novamente? (s/n)').lower()
        if rodar_novamente not in ('s', 'n'):
            print('Por favor, selecione "s" ou "n"')
            self.rodarNovamente()
        if rodar_novamente == 's':
            self.Iniciar()
        if rodar_novamente == 'n':
            print('O programa esta sendo fechado...')
            time.sleep(3)
            print('Programa encerrado!')


curso = PrimeiroCliente()
curso.Iniciar()
