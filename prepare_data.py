import notion_api

patient_information={
        "form_name": "",
        "form_tray": "",
        "form_redo": "",
        "form_redo_type":"",
        "form_redo_patient":"",
        "form_redo_ordern":""
    }
prescription_type={
        "form_single_vision": "",
        "form_multifocals": "",
        "form_progressives": "",
        "form_freeform": "",
    } 
    
enter_prescription={
       "form_rxside": "PAIR/Both Eyes",
       "right_eye":{
            "form_sph_rt": "",
            "form_cyl_rt": "",
            "form_axis_rt": "",
            "form_add_rt": "",
            "form_seg_rt": "",
            "form_prism1_rt" : "",
            "form_prism4_rtIN" : "",
            "form_prism3_rt" : "",
            "form_prism4_rt": "",
            "form_far_rt" : "",
            "form_near_rt": "",
        },
        "left_eye":{
            "form_sph_lt": "",
            "form_cyl_lt": "",
            "form_axis_lt": "",
            "form_add_lt" : "",
            "form_seg_lt" : "",
            "form_prism1_lt": "",
            "form_prism4_ltIN":"",
            "form_prism3_lt":"",
            "form_prism4_lt": "",
            "form_far_lt" : "",
            "form_near_lt": "",
        }
    }
frame_data={
        "form_supply_frame": "",
        "form_later_frame" : "yes",
        "form_uncut_frame" : "",
        "Frame_Options" : "Zyl Edge",
        "form_enclosed" :"False",
}

frames_catalog_data={
        "select":{
        "form_model_dd":"",
        "form_size_dd":"",
        "form_color_dd":""
        },
        "form_frame_model":"",
        "form_frame_color":"",
        "form_eye_size_a":"",
        "form_eye_size_b":"",
        "form_frame_dbl":"",
        "form_frame_ed": ""
    }
lens_material={
       "form_cr39" : "",
       "form_156" : "",
       "form_160" : "",
       "form_167":"",
       "form_174":"",
       "form_trivex":"",
       "form_156_blue":"",
       "form_167_blue" :"",
       "form_156_blue": "",
       "form_polycarbonate" :"yes",
       "form_polycarbonate_blue": ""
    }
lens_colors_coatings={
        "uncoated":{
        "form_uncoat" : "yes",
        "form_ar": "Sapphire AR",
        "form_photochromic": "",
        "form_tint_first" : "",
        "form_tint_color" : "",
        "form_grade" : "",
        "form_polarized" : "",
        "form_ar_side": "",
        "form_scratch_coat" : ""},
        "form_mirror_info":{
           "form_mirror" : "",
           "form_mirror_color": "",
           "form_mirror_grade": "",
        }
    }
comment={
        "comments": ""
    }

def fetch_data():
     # requested_data=[{}]
    requested_data=notion_api.get_data()
    if requested_data:
        prepar_dict(requested_data)
    else:
        print("No Data Found")    
        

def prepar_dict(requested_data):
    for request in requested_data:
        for key ,value in request.items():
            if key =="client_name":
                patient_information["form_name"]=value
            elif key =="Lens Type":
                prescription_type["form_single_vision"]=value
            elif key =="OD - SPH":
                enter_prescription.get("right_eye")["form_sph_rt"]=value 
            elif key =="OD - CYL":
                enter_prescription.get("right_eye")["form_cyl_rt"]=value 
            elif key =="OD - Axis":
                enter_prescription.get("right_eye")["form_axis_rt"]=value    
            elif key =="OD - PD (Distance)":
                enter_prescription.get("right_eye")["form_far_rt"]=value 
            elif key =="OD - PD (Near)":
                enter_prescription.get("right_eye")["form_near_rt"]=value     
            elif key =="OS - SPH":
                enter_prescription.get("left_eye")["form_sph_lt"]=value   
            elif key =="OS - CYL":
                enter_prescription.get("left_eye")["form_cyl_lt"]=value 
            elif key =="OS - Axis":
                enter_prescription.get("left_eye")["form_axis_lt"]=value    
            elif key =="OS - PD (Distance)":
                enter_prescription.get("left_eye")["form_far_lt"]=value 
            elif key =="OS - PD (Near)":
                enter_prescription.get("left_eye")["form_near_lt"]=value
            elif key =="Model":
                frames_catalog_data["form_frame_model"]=value    
            elif key =="Color":
                frames_catalog_data["form_frame_color"]=value 
            elif key =="Frame Size - A":
                frames_catalog_data["form_eye_size_a"]=value
            elif key =="Frame Size - B":
                frames_catalog_data["form_eye_size_b"]=value    
            elif key =="Frame Size - DBL":
                frames_catalog_data["form_frame_dbl"]=value 
            elif key =="Frame Size - ED":
                frames_catalog_data["form_frame_ed"]=value
            elif key =="Notes":
                comment["comments"]=value        