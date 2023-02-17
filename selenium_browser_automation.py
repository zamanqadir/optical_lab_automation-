from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import configuration
import prepare_data


# dr

def initialise():
    options = Options()
    options.add_experimental_option("detach" , True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get(configuration.initial_link)
    driver.maximize_window()
    return driver

def login(driver):
    
    login_email=driver.find_element(By.NAME , "email")
    if login_email:
        login_email.send_keys(configuration.admin_email)
        login_password=driver.find_element(By.NAME , "password")   
        if login_password:
            login_password.send_keys(configuration.admin_password)
        login_button=driver.find_element("xpath" ,"//input[@type='submit']")
        if login_button:
           login_button.click()
            

def go_to_lab_job(driver):
    
    lab_job_link=driver.find_element("xpath" ,"//a[text()='Lab Job']")
    driver.implicitly_wait(10)
    if lab_job_link:
       driver.execute_script("arguments[0].click();",lab_job_link)
        


def fill_out_patient_information(patient_information,driver):

    # fill out fields if fields exists

    form_name=driver.find_element(By.ID, "form_name")
    if form_name:
        form_name.send_keys(patient_information.get('form_name'))
    
    form_tray=driver.find_element(By.ID, "form_tray")
    if form_tray:
        form_tray.send_keys(patient_information.get('form_tray'))
    
    form_redo=driver.find_element(By.ID, "form_redo")
    if form_redo and patient_information.get('form_redo') == "yes" :
        driver.find_element(By.ID, "form_redo").click()
         
        form_redo_type=driver.find_element(By.ID, "form_redo_type")
        if form_redo_type:
            form_redo_type.send_keys(patient_information.get('form_redo_type'))
        
        form_redo_patient=driver.find_element(By.CLASS_NAME, "chosen-search-input")
        if form_redo_patient:
            form_redo_patient.send_keys(patient_information.get('form_redo_patient'))

        form_redo_ordern=driver.find_element(By.ID, "form_redo_ordern")
        if form_redo_ordern:
            form_redo_ordern.send_keys(patient_information.get('form_redo_ordern'))  

def fill_out_prescription_type(prescription_type,driver):

    for key ,value in prescription_type.items():
        form_ptkey=driver.find_element(By.ID, key)
        if form_ptkey:
            form_ptkey.send_keys(value)
    
     
def fill_out_enter_prescription(enter_prescription,driver):

    #question here   
    rx_side=enter_prescription.get('form_rxside')
    form_rxside=driver.find_element(By.ID, "form_rxside")
    if form_rxside:
            form_rxside.send_keys(enter_prescription.get('form_rxside'))  
       
    if rx_side=="Right Eye only":
        right_eye_data=enter_prescription.get('right_eye')
        fill_right_eye(right_eye_data , driver)
       
    elif rx_side=="Left Eye only":
        left_eye_data=enter_prescription.get('left_eye')
        fill_left_eye(left_eye_data, driver)
       
    elif rx_side=="PAIR/Both Eyes":
        right_eye_data=enter_prescription.get('right_eye')
        fill_right_eye(right_eye_data , driver)
        left_eye_data=enter_prescription.get('left_eye')
        fill_left_eye(left_eye_data,driver)
            
def fill_right_eye(right_eye_data , driver):

     for key ,value in right_eye_data.items():
        form_rkey=driver.find_element(By.ID, key)
        if form_rkey:
            form_rkey.send_keys(value)          


def fill_left_eye(left_eye_data,driver):

    for key ,value in left_eye_data.items():
        form_lkey=driver.find_element(By.ID, key)
        if form_lkey:
            form_lkey.send_keys(value)
    
def fill_out_frame_data(frame_data,driver):
    
    for key ,value in frame_data.items():
        form_fdkey=driver.find_element(By.ID, key)
      
        if form_fdkey and key=="form_supply_frame" and value=="yes":
            form_fdkey.click()
        
        elif form_fdkey and key=="Frame_Options":
            form_fdkey.send_keys(value)
        
        elif key=="form_enclosed" and value=="yes":
            form_fdkey.click()

        elif key!="form_supply_frame" and key!="Frame_Options" and key!="form_enclosed" and value=="yes":    
            form_fdkey.click()
            alert = Alert(driver)
            alert.accept()

def fill_out_frames_catalog_info(frames_catalog_data,select_cate,driver):
   
    for key ,value in frames_catalog_data.items():
        if key=="select" and select_cate=="yes":
            select_cat_from_drop(frames_catalog_data.get("select"),driver)
        elif key!="select":
           form_fckey=driver.find_element(By.ID, key)
           form_fckey.send_keys(value)

def select_cat_from_drop(select,driver):
     for key ,value in select.items():
        form_skey=driver.find_element(By.ID, key)
        if form_skey:
            form_skey.send_keys(value)

def fill_out_lens_material_info(lens_material,driver):
      for key ,value in lens_material.items():
        form_lmkey=driver.find_element(By.ID, key)
        if form_lmkey and value=="yes":
            form_lmkey.click()


def fill_lens_colors_coatings_info(lens_colors_coatings, driver):
    for key ,value in lens_colors_coatings.items():
        if key=="uncoated":
             fill_uncoated_info(value,driver)
        else:
          fill_mirror_info(value,driver)
        

def fill_uncoated_info(uncoated_info,driver):
    # problem here
    for key,value in uncoated_info.items():
        form_skey=driver.find_element(By.ID, key)
    
        if key == "form_uncoat" and value=="no":
            return
        elif key == "form_uncoat" and value=="yes":
            if form_skey:
                form_skey.send_keys(value)
        elif key != "form_uncoat" and uncoated_info.get('form_uncoat')=="no":  
            if form_skey:
                form_skey.send_keys(value)

def fill_mirror_info(form_mirror_info,driver):
    if form_mirror_info.get('form_mirror') == "yes" :

        form_mirror=driver.find_element(By.ID, "form_mirror")
        if form_mirror:
            form_mirror.click()
        form_mirror_color=driver.find_element(By.ID, "form_mirror_color")    
        if form_mirror_color:   
           form_mirror_color.send_keys(form_mirror_info.get('form_mirror_color'))

        form_mirror_grade=driver.find_element(By.ID, "form_mirror_grade")
        if form_mirror_grade:
           form_mirror_grade.send_keys(form_mirror_info.get('form_mirror_grade'))

def fill_out_comments(comment,driver):
     for key ,value in comment.items():
        form_skey=driver.find_element(By.NAME, key)
        if form_skey:
            form_skey.send_keys(value)


def review_button_click(email,driver):
    review_button=driver.find_element(By.ID,'prview_button3')
    if review_button:
       review_button.click()
       fill_out_email(email ,driver)

def fill_out_email(email ,driver):
     email_field=driver.find_element(By.ID, 'email2')
     if email_field:
         email_field.send_keys(email)
         add_button_click(driver)

def add_button_click(driver):
    email=driver.find_element(By.ID, 'email2').get_attribute("value")
    add_button=driver.find_element(By.ID,'order_submit')
    if email and add_button:
        driver.stop()
        add_button.click()
    

def main():
    
    prepare_data.fetch_data()     
    driver=initialise()
    login(driver)
    go_to_lab_job(driver)
    fill_out_patient_information(prepare_data.patient_information , driver)
    fill_out_prescription_type(prepare_data.prescription_type,driver)
    fill_out_enter_prescription(prepare_data.enter_prescription,driver)
    fill_out_frame_data(prepare_data.frame_data,driver)
    select_cate=prepare_data.frame_data.get("form_supply_frame")
    fill_out_frames_catalog_info(prepare_data.frames_catalog_data,select_cate,driver)
    fill_out_lens_material_info(prepare_data.lens_material,driver)
    fill_lens_colors_coatings_info(prepare_data.lens_colors_coatings ,driver)
    fill_out_comments(prepare_data.comment,driver)
    
   
    # email="null@yopmail.com"
    # review_button_click(email,driver)

main()    