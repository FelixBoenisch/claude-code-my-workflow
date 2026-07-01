#!/usr/bin/env python3
"""Reconcile OCR'd Prolific submission rows (from PNGs) against the accurate
ID lists in the per-study PDF invoices, and emit a clean CSV.

started / time_taken / bonus are transcribed from the PNGs (only source).
prolific_id is OCR'd from the PNG then snapped to the nearest exact ID in the
SAME study's PDF candidate set (difflib). Rows whose ID does not match a PDF
candidate (e.g. NO CODE / returned rows not on the invoice) keep the OCR'd ID
and are flagged id_source=ocr_only.
"""
import csv, glob, re, subprocess, difflib, os

HERE = os.path.dirname(os.path.abspath(__file__))

# png_file -> pdf invoice that contains that study's approved IDs
STUDY_PDF = {
    "pre pilot delegator.png":            "pre pilot delegator.pdf",
    "pre pilot evaluator.png":            "pre pilot evaluator.pdf",
    "pilot delegator.png":                "pilot delegator.pdf",
    "pilot delegator 2.png":              "pilot delegator 2.pdf",
    "pilot evaluator.png":                "pilot evaluator.pdf",
    "pilot evaluator 2.png":              "pilot evaluator 2.pdf",
    "pilot evaluator 3.png":              "pilot evaluator 3.pdf",
    "Main I - dela.png":                  "Main I - del.pdf",
    "Main I - del - no punisha.png":      "Main I - del - no punish.pdf",
    "Main I - del - no punishb.png":      "Main I - del - no punish.pdf",
    "Main I - del - no punishc.png":      "Main I - del - no punish.pdf",
    "Main I - del - no punish2.png":      "Main I - del - no punish2.pdf",
    "Main I - evaa.png":                  "Main I - eva.pdf",
    "Main I - evab.png":                  "Main I - eva.pdf",
    "Main I - eva2.png":                  "Main I - eva2.pdf",
    "Main I - eva3.png":                  "Main I - eva3.pdf",
    "Main I - eva4.png":                  "Main I - eva 4.pdf",
    "Main I - no punish - eva1a.png":     "Main I - no punish - eva1.pdf",
    "Main I - no punish - eva2.png":      "Main I - no punish - eva2.pdf",
    "Main I - no punish - eva3.png":      "Main I - no punish - eva3.pdf",
    "Main I - no punish - eva4.png":      "Main I - no punish - eva4.pdf",
    "Main I - no punish - eva5.png":      "Main I - no punish - eva5.pdf",
}

def pdf_ids(pdf):
    txt = subprocess.run(["pdftotext","-layout",os.path.join(HERE,pdf),"-"],
                         capture_output=True,text=True).stdout
    return sorted(set(re.findall(r"[0-9a-f]{24}", txt)))

# RAW transcriptions: (png_file, ocr_id, started, time_taken, bonus)
# bonus "" = blank/NO CODE in the dashboard.
RAW = [
 # --- pre-pilot ---
 ("pre pilot delegator.png","56ca31b2e939d1000cbaf5cb","26 Feb 2023 02:11","00:12:14","3.00"),
 ("pre pilot evaluator.png","5ccb343fcdcf0f0001ba779e","26 Feb 2023 03:40","00:07:06","4.90"),
 # --- pilot delegator (19) ---
 ("pilot delegator.png","63d189e4ac39d0622f4c8e3d","26 Feb 2023 14:01","00:08:49","4.05"),
 ("pilot delegator.png","59d4d493c618a50001cf5c6a","26 Feb 2023 14:01","00:16:07","5.30"),
 ("pilot delegator.png","5cbacd419bb663000137721c","26 Feb 2023 14:03","00:10:51","2.80"),
 ("pilot delegator.png","5ed1463ba41e260775f2ec6c","26 Feb 2023 14:05","00:14:53","2.50"),
 ("pilot delegator.png","5bda214348428800013070ba","26 Feb 2023 14:05","00:08:15","3.35"),
 ("pilot delegator.png","604633f72d9cdc0a1b04fc3c","26 Feb 2023 14:06","00:09:52","2.50"),
 ("pilot delegator.png","629265c60618aa54bb11c2bf","26 Feb 2023 14:06","00:07:34","1.50"),
 ("pilot delegator.png","634700f816868644b1f51b9e","26 Feb 2023 14:07","00:07:01",""),
 ("pilot delegator.png","622a2e482bfab3405f7c5ae9","26 Feb 2023 14:07","00:06:31","3.00"),
 ("pilot delegator.png","62b2476fc924f1a048bd412b","26 Feb 2023 14:07","00:17:49","4.30"),
 ("pilot delegator.png","61071a2b7edf61e912210b2","26 Feb 2023 14:07","00:19:52","2.00"),
 ("pilot delegator.png","6319fb98fc610c552ae07a5d","26 Feb 2023 14:09","00:07:37","3.00"),
 ("pilot delegator.png","61668d00d12cac88caa9186e","26 Feb 2023 14:10","00:09:32","2.00"),
 ("pilot delegator.png","6346898b38625b0d3494ca32","26 Feb 2023 14:12","00:10:29","3.10"),
 ("pilot delegator.png","5baa21188a01680001ff1a6f","26 Feb 2023 14:13","00:14:07","2.50"),
 ("pilot delegator.png","5c6092ac4cc94200016a61be","26 Feb 2023 14:13","00:08:11","0.50"),
 ("pilot delegator.png","634a7bbcac6f28ed59e5bd59","26 Feb 2023 14:13","00:11:40","0.70"),
 ("pilot delegator.png","5af528c2a0603b16a793423d","26 Feb 2023 14:19","00:11:36","0.70"),
 ("pilot delegator.png","60da3c34940c209d729e32b8","26 Feb 2023 14:25","00:12:05","2.80"),
 # --- pilot delegator 2 (8) ---
 ("pilot delegator 2.png","57db358d631235000138ab6f","26 Feb 2023 22:30","00:08:36","3.00"),
 ("pilot delegator 2.png","6102fcaa8a324aaf83f7fa8c","26 Feb 2023 22:33","00:12:53","1.70"),
 ("pilot delegator 2.png","60fd19fc1152c0b4056a73e0","26 Feb 2023 22:33","00:10:58",""),
 ("pilot delegator 2.png","5caa3731d439ae001a5965b2","26 Feb 2023 22:34","00:10:46","2.50"),
 ("pilot delegator 2.png","629c11c0d89e0c18f21a687a","26 Feb 2023 22:36","00:13:52","0.50"),
 ("pilot delegator 2.png","63d044a4c63272db35625084","26 Feb 2023 22:37","00:27:48","3.60"),
 ("pilot delegator 2.png","62cae5d244b7a060b567217a","26 Feb 2023 22:39","00:10:05","2.80"),
 ("pilot delegator 2.png","5fc110a22738afafb8109236","26 Feb 2023 22:40","00:06:35","3.30"),
 # --- pilot evaluator (17) ---
 ("pilot evaluator.png","601b0712b0701c46459aab27","26 Feb 2023 23:41","00:14:20","1.10"),
 ("pilot evaluator.png","611ffc2ea28a21fa3367fd4c","26 Feb 2023 23:41","00:04:26","5.40"),
 ("pilot evaluator.png","6311f718025bf2d9641bbb33","26 Feb 2023 23:42","00:04:49","1.10"),
 ("pilot evaluator.png","5a8b8a0a380f900589c2ace4","26 Feb 2023 23:43","00:04:37","0.80"),
 ("pilot evaluator.png","5f2aad6868d6c232aebd20aa","26 Feb 2023 23:43","00:15:59","4.50"),
 ("pilot evaluator.png","59af9ba762637600014a873d","26 Feb 2023 23:43","00:12:39","1.40"),
 ("pilot evaluator.png","5cf7b7c9a7af560001769788","26 Feb 2023 23:44","00:09:38","1.40"),
 ("pilot evaluator.png","63d44d95747a20db09a38151","26 Feb 2023 23:44","00:08:50","4.90"),
 ("pilot evaluator.png","63ea5822abbd0f51cfb05b23","26 Feb 2023 23:46","00:05:19","4.60"),
 ("pilot evaluator.png","6321d74ca80fe8632af0b5ae","26 Feb 2023 23:47","00:06:01","1.30"),
 ("pilot evaluator.png","6272859947cff7c57fb2afc4","26 Feb 2023 23:48","00:14:40",""),
 ("pilot evaluator.png","637f89ffcbf20bd680c0d79e","26 Feb 2023 23:48","00:12:28","0.90"),
 ("pilot evaluator.png","5c62c668d4899e00015ca4c9","26 Feb 2023 23:48","00:04:54","0.80"),
 ("pilot evaluator.png","62b7574f10d88d4f6898f5d6","26 Feb 2023 23:48","00:06:51","0.50"),
 ("pilot evaluator.png","60ce601b0db7f30595a36acd","26 Feb 2023 23:50","00:11:33","1.00"),
 ("pilot evaluator.png","62b444cb2f1d7c410e12f21c","26 Feb 2023 23:51","00:03:15","1.30"),
 ("pilot evaluator.png","5fe22499bbdf7fd5ae926b26","26 Feb 2023 23:51","00:05:55","1.30"),
 # --- pilot evaluator 2 (8) ---
 ("pilot evaluator 2.png","5d4a048fcc60c20001ddbbde","27 Feb 2023 10:52","00:10:28","0.90"),
 ("pilot evaluator 2.png","6294f4e1a0672904cad02d71","27 Feb 2023 10:53","00:05:04",""),
 ("pilot evaluator 2.png","5dd6d94cbca2a466ca211b0d","27 Feb 2023 10:56","00:05:56","0.60"),
 ("pilot evaluator 2.png","6033c1abdc90b513004b6d95","27 Feb 2023 10:56","00:08:23","5.30"),
 ("pilot evaluator 2.png","5eda4380f848290674f0f166f","27 Feb 2023 10:58","00:04:56","1.10"),
 ("pilot evaluator 2.png","5e52584cc9f6062582d99041","27 Feb 2023 11:00","00:04:53","1.10"),
 ("pilot evaluator 2.png","62d5b0e01a9316211e849a23","27 Feb 2023 11:02","00:05:08","1.10"),
 ("pilot evaluator 2.png","627125a4c8bbe00988850330","27 Feb 2023 11:03","00:06:57","1.10"),
 # --- pilot evaluator 3 (2) ---
 ("pilot evaluator 3.png","63d3fbdc74f911908d4c50b3","28 Feb 2023 13:18","00:06:33","4.10"),
 ("pilot evaluator 3.png","5f1fe390defled00093b8d7c","28 Feb 2023 13:20","00:07:01","0.90"),
 # --- Main I - dela (top of 53) ---
 ("Main I - dela.png","59303adcdb68d70001ecd942","19 Jun 2023 14:31","00:14:31","2.30"),
 ("Main I - dela.png","5be1aac8ca095c0001b9f6e4","19 Jun 2023 14:46","00:07:18","2.00"),
 ("Main I - dela.png","5f091bb928d2f41aa5ed3137","19 Jun 2023 14:57","00:12:02","2.30"),
 ("Main I - dela.png","62b8430064f1514d058fa23d","19 Jun 2023 14:59","00:12:00","1.00"),
 ("Main I - dela.png","5d566fa918f22f000148d118","19 Jun 2023 15:09","00:06:37","1.85"),
 ("Main I - dela.png","5f341e306c067e1255643375","19 Jun 2023 15:09","00:09:30","2.00"),
 ("Main I - dela.png","5d3f7f33eb67080001cd7250","19 Jun 2023 15:10","00:14:45","2.00"),
 ("Main I - dela.png","5a4698b97a3e3a0001dd564e","19 Jun 2023 15:10","00:05:05",""),
 ("Main I - dela.png","61002bb71b66ea88772a39f3","19 Jun 2023 15:14","00:12:37","2.30"),
 ("Main I - dela.png","5f9c763b3fb22a1261f6650e","19 Jun 2023 15:15","00:13:06","4.30"),
 ("Main I - dela.png","5e7796db39c441307fc438a7","19 Jun 2023 15:19","00:20:09","4.30"),
 ("Main I - dela.png","5a4e68fb30adf7000106fc6f","19 Jun 2023 15:22","00:09:17","1.80"),
 ("Main I - dela.png","5997e57d6b939900012da0e2","19 Jun 2023 15:23","00:23:50","2.90"),
 ("Main I - dela.png","6148bf5997774b8538b13c68","19 Jun 2023 15:23","00:17:08","2.00"),
 ("Main I - dela.png","58ee2d957b2e410001c2e807","19 Jun 2023 15:24","00:22:10","2.30"),
 ("Main I - dela.png","612a3d97a2cc259f7ff9b580","19 Jun 2023 15:25","00:14:06","3.00"),
 ("Main I - dela.png","5aae762bc4e8f200014b3f88","19 Jun 2023 15:26","00:17:26","2.95"),
 ("Main I - dela.png","57cdc1afa4804100018b5c34","19 Jun 2023 15:29","00:10:14","4.30"),
 ("Main I - dela.png","5f7ca9b13e20031150440b98","19 Jun 2023 15:30","00:26:18","2.30"),
 # --- Main I - del - no punisha (19) ---
 ("Main I - del - no punisha.png","5ee3c87b71f86b08dabea79c","19 Jun 2023 20:28","00:14:56","2.00"),
 ("Main I - del - no punisha.png","610ba90131eb1a27f1b6ec8c","19 Jun 2023 20:31","00:06:39","2.00"),
 ("Main I - del - no punisha.png","5b28df1a2bc7780001c2322f","19 Jun 2023 20:37","00:08:46","2.00"),
 ("Main I - del - no punisha.png","5ed925860adb8b46a34a0d1a","19 Jun 2023 20:41","00:11:35","2.30"),
 ("Main I - del - no punisha.png","5855878ec41fd900014345d4","19 Jun 2023 20:42","00:10:21","4.30"),
 ("Main I - del - no punisha.png","60e69b85a707ad939f1dde11","19 Jun 2023 20:44","00:09:25","2.30"),
 ("Main I - del - no punisha.png","5db2cfccc80c2b00220ec9e5","19 Jun 2023 20:44","00:17:11","3.00"),
 ("Main I - del - no punisha.png","5fad5245ca80c102cff61069","19 Jun 2023 20:44","00:11:51","2.00"),
 ("Main I - del - no punisha.png","6096dee4df7f250e5ba9d78d","19 Jun 2023 20:46","00:08:50","3.00"),
 ("Main I - del - no punisha.png","60cfd66e2cc5d72d75bc9839","19 Jun 2023 20:50","00:12:51","3.30"),
 ("Main I - del - no punisha.png","5f56bfb85619fa12df98d7d7","19 Jun 2023 20:58","00:11:42","2.00"),
 ("Main I - del - no punisha.png","59aaa1000acd5600012ebfb5","19 Jun 2023 21:05","00:13:53","2.30"),
 ("Main I - del - no punisha.png","588126f90234ec00016eff60","19 Jun 2023 21:08","00:08:49","2.00"),
 ("Main I - del - no punisha.png","5b95819daa1729000192b956","19 Jun 2023 21:09","00:13:19","2.00"),
 ("Main I - del - no punisha.png","63d820d4711332d56473bd98","19 Jun 2023 21:10","00:12:38","2.00"),
 ("Main I - del - no punisha.png","5fb997d62e675a62d4512560","19 Jun 2023 21:13","00:12:02","4.30"),
 ("Main I - del - no punisha.png","5c38dab0f0ae4c00011238c1","19 Jun 2023 21:13","00:11:28","2.00"),
 ("Main I - del - no punisha.png","6176b6cf6393051a796fee4d","19 Jun 2023 21:14","00:06:21","2.30"),
 ("Main I - del - no punisha.png","631123376033bb148edc0ebb","19 Jun 2023 21:16","00:18:15","2.30"),
 # --- Main I - del - no punishb (continuation) ---
 ("Main I - del - no punishb.png","5da718379d0c290014c98357","19 Jun 2023 21:17","00:05:50","4.30"),
 ("Main I - del - no punishb.png","5da352abffef8000150eca23","19 Jun 2023 21:17","00:16:39","2.00"),
 ("Main I - del - no punishb.png","6020329e88ba9160b200b96b","19 Jun 2023 21:18","00:09:03","4.00"),
 ("Main I - del - no punishb.png","615e0029921e403470fd8272","19 Jun 2023 21:21","00:11:37","2.00"),
 ("Main I - del - no punishb.png","60a0fa7c78f0ecce1f9d8a65","19 Jun 2023 22:00","00:12:28","2.00"),
 ("Main I - del - no punishb.png","64415bcdc97b9b266459aed7","19 Jun 2023 22:01","00:11:52","2.00"),
 ("Main I - del - no punishb.png","5cbf6908d074ee00016accb2","19 Jun 2023 22:05","00:14:45","2.30"),
 ("Main I - del - no punishb.png","5f54b7bc649418811db24711","19 Jun 2023 22:17","00:08:29","4.00"),
 ("Main I - del - no punishb.png","56e5adeab2093a000d4f18d2","19 Jun 2023 22:17","00:14:23","2.30"),
 ("Main I - del - no punishb.png","5e98ccf370194e0f49a1333b","19 Jun 2023 22:25","00:13:25","2.00"),
 ("Main I - del - no punishb.png","63e51d0dedeebfa7950e7d6a","20 Jun 2023 13:06","00:15:56","2.50"),
 ("Main I - del - no punishb.png","6384dfb0cfe3f1ba71f9ad11","20 Jun 2023 13:17","00:13:10","4.00"),
 ("Main I - del - no punishb.png","644a9b73b330d90e0b970dba","20 Jun 2023 13:17","00:10:16","4.30"),
 ("Main I - del - no punishb.png","64610526db3f73f93d08710a","20 Jun 2023 13:20","00:17:03","4.00"),
 ("Main I - del - no punishb.png","637ffd0ae752c8e33f91798b","20 Jun 2023 13:25","00:07:55","2.30"),
 ("Main I - del - no punishb.png","5d2df1ce54cf6d0001df7e17","20 Jun 2023 13:29","00:05:08","2.00"),
 ("Main I - del - no punishb.png","6310d187315505a30722cd64","20 Jun 2023 13:38","00:11:06","2.30"),
 ("Main I - del - no punishb.png","63191a142fc45c3bf7036510","20 Jun 2023 13:39","00:09:30","2.80"),
 ("Main I - del - no punishb.png","63d41c63af65d54621b0d37a","20 Jun 2023 13:46","00:10:16","4.00"),
 ("Main I - del - no punishb.png","5c7cf4e3ac90ae000144c9b9","20 Jun 2023 13:49","00:08:48","2.00"),
 ("Main I - del - no punishb.png","63d7d315ebf6c98c92c2a7a1","20 Jun 2023 13:52","00:15:26","2.00"),
 ("Main I - del - no punishb.png","5e5441f2c65ccb44a4e3d463","20 Jun 2023 13:59","00:08:49","2.30"),
 ("Main I - del - no punishb.png","62d28f109e5c437c89dac211","20 Jun 2023 14:03","00:08:43","2.00"),
 ("Main I - del - no punishb.png","604f684950227bd07a37376d","20 Jun 2023 14:56","00:08:18","2.00"),
 ("Main I - del - no punishb.png","60033122542fe9034f69fce9","20 Jun 2023 15:09","00:06:59","4.00"),
 ("Main I - del - no punishb.png","5c80e889a1d4b900114f2be3","20 Jun 2023 15:09","00:16:05","4.30"),
 ("Main I - del - no punishb.png","61518deddeaeef3d2d107c38","20 Jun 2023 15:10","00:12:53","4.00"),
 # --- Main I - del - no punishc (continuation) ---
 ("Main I - del - no punishc.png","5dbefec9f8e3f93a249ed04a","20 Jun 2023 15:15","00:10:31","2.50"),
 ("Main I - del - no punishc.png","6346b94a5fbbc84d41ec14fb","20 Jun 2023 15:17","00:20:59",""),
 ("Main I - del - no punishc.png","5e277e5b5f39769bacb46101","20 Jun 2023 15:20","00:14:59","2.00"),
 ("Main I - del - no punishc.png","62b6cb277460cccbc8f27ad5","20 Jun 2023 15:20","00:20:21","4.00"),
 ("Main I - del - no punishc.png","5a65011f63394a0001556857","20 Jun 2023 15:21","00:11:10","2.00"),
 ("Main I - del - no punishc.png","645514dc6131c93e54f0792f","20 Jun 2023 15:22","01:16:02","4.00"),
 ("Main I - del - no punishc.png","5ef34cc943115906d6aa397f","20 Jun 2023 15:24","00:12:07","2.30"),
 ("Main I - del - no punishc.png","5d51bd30f334bf00011f7e4b","20 Jun 2023 15:27","00:12:57","2.00"),
 ("Main I - del - no punishc.png","5d416bd5af929100194e80e1","20 Jun 2023 15:29","00:11:00","2.30"),
 ("Main I - del - no punishc.png","63e00673acb154c72d564dd1","20 Jun 2023 15:30","00:12:14","4.30"),
 ("Main I - del - no punishc.png","5d64dab1f1c6780001fff01e","20 Jun 2023 15:31","00:12:00","2.00"),
 ("Main I - del - no punishc.png","64406228450534e2b06b72a4","20 Jun 2023 15:32","00:10:13","2.00"),
 ("Main I - del - no punishc.png","5e3b07fddc4a3431fbcc6235","20 Jun 2023 15:36","00:06:18","4.30"),
 ("Main I - del - no punishc.png","5f034e4e4e80ca2344b11ae1","20 Jun 2023 15:37","00:06:45","2.00"),
 ("Main I - del - no punishc.png","5f102f0212ea4f000a8ac9da","20 Jun 2023 15:37","00:09:32","4.00"),
 # --- Main I - del - no punish2 (20) ---
 ("Main I - del - no punish2.png","5a1da3d67ecfc50001be28e4","21 Jun 2023 08:13","00:07:45","4.00"),
 ("Main I - del - no punish2.png","62717bd9ccd926c3a84ec5b2","21 Jun 2023 08:13","00:10:05","2.50"),
 ("Main I - del - no punish2.png","5d86fbe77e54b0001a80fd8b","21 Jun 2023 08:18","00:20:14","4.00"),
 ("Main I - del - no punish2.png","63e151b982d3d7fc75c50a5b","21 Jun 2023 08:20","00:10:51","4.30"),
 ("Main I - del - no punish2.png","63dad9e2dd58781d74bfa642","21 Jun 2023 08:22","00:11:53","2.00"),
 ("Main I - del - no punish2.png","5f10d13957b4763f401690e5","21 Jun 2023 08:22","00:19:23","2.30"),
 ("Main I - del - no punish2.png","5af0e378e1b5b8000148a38d","21 Jun 2023 08:22","00:07:54","2.00"),
 ("Main I - del - no punish2.png","6481c18b731c471182a550ae","21 Jun 2023 08:25","00:09:26","4.00"),
 ("Main I - del - no punish2.png","6158bd6a0ff7b28732f8398a","21 Jun 2023 08:26","00:13:07","4.30"),
 ("Main I - del - no punish2.png","644e195eb24217e7b414a673","21 Jun 2023 08:28","00:11:27","4.00"),
 ("Main I - del - no punish2.png","567c1cc8b7d79a0012b273ef","21 Jun 2023 08:28","00:14:13","2.00"),
 ("Main I - del - no punish2.png","5cff4ed26d6326001acf7022","21 Jun 2023 08:29","00:07:21","2.00"),
 ("Main I - del - no punish2.png","63d439df44f39695eef3023e","21 Jun 2023 08:29","00:12:36","4.30"),
 ("Main I - del - no punish2.png","60c770c2798ff49897e4826a","21 Jun 2023 08:30","00:12:34","2.30"),
 ("Main I - del - no punish2.png","6447ccd602f2904fd0b846d7","21 Jun 2023 08:30","00:10:46","2.00"),
 ("Main I - del - no punish2.png","615df15772fbf6ba104032fe","21 Jun 2023 08:30","00:14:48","2.00"),
 ("Main I - del - no punish2.png","64135994fa1c09f8a0b91b95","21 Jun 2023 08:31","00:13:22","2.00"),
 ("Main I - del - no punish2.png","62ad6daf3d02cb55ddf12c6a","21 Jun 2023 08:32","00:10:25","4.00"),
 ("Main I - del - no punish2.png","62b57d34b7bdc2d0835fab76","21 Jun 2023 08:32","00:05:01","2.00"),
 ("Main I - del - no punish2.png","63038022102690944a6720cf","21 Jun 2023 08:34","00:08:51","2.30"),
 # --- Main I - evaa (top of 37) ---
 ("Main I - evaa.png","603b0a1641a4cc7273d3e7da","19 Jun 2023 17:47","00:07:00","4.10"),
 ("Main I - evaa.png","5cce82dc8c978d00157c534a","19 Jun 2023 17:48","00:06:29","0.40"),
 ("Main I - evaa.png","5ed2717aec79fd1d3ca47d65","19 Jun 2023 17:50","00:11:33","0.60"),
 ("Main I - evaa.png","61620c697493fd1f0e57a700","19 Jun 2023 17:56","00:05:32","4.40"),
 ("Main I - evaa.png","552a8dd1fdf99b4e4716e81b","19 Jun 2023 18:00","00:04:02","0.90"),
 ("Main I - evaa.png","5fc7f97d984e250e0954d565","19 Jun 2023 18:00","00:05:13","0.40"),
 ("Main I - evaa.png","5f2ed247fc40b227293a1a5e","19 Jun 2023 18:02","00:06:29","0.10"),
 ("Main I - evaa.png","5e8d0c7d40d8520da1903a86","19 Jun 2023 18:03","00:05:34","0.10"),
 ("Main I - evaa.png","59b85e50d793b40001459a2f","19 Jun 2023 18:03","00:03:11","0.10"),
 ("Main I - evaa.png","5b9281970ff8eb00018874f9","19 Jun 2023 18:09","00:05:10","0.10"),
 ("Main I - evaa.png","595133ca2e0323000136855a","19 Jun 2023 18:10","00:12:13","0.30"),
 ("Main I - evaa.png","54b1e80cfdf99b0b3d806352","19 Jun 2023 18:10","00:03:07","4.00"),
 ("Main I - evaa.png","5e7dfc715acd1402882e93eb","19 Jun 2023 18:11","00:08:02","0.10"),
 ("Main I - evaa.png","5af53b822029970001 6d1a1b".replace(" ",""),"19 Jun 2023 18:11","00:04:19","0.10"),
 ("Main I - evaa.png","5cfa8766825511000129d41e","19 Jun 2023 18:13","00:06:59","5.10"),
 ("Main I - evaa.png","5e20ac9fd911313b03c54832","19 Jun 2023 18:18","00:06:31","4.30"),
 ("Main I - evaa.png","5aa8bd26f6dfdd0001eb1a9e","19 Jun 2023 18:18","00:11:07","4.00"),
 ("Main I - evaa.png","59400de88fcebc0001075a41","19 Jun 2023 18:19","00:08:09","0.40"),
 ("Main I - evaa.png","597f786b2c08900001963acc","19 Jun 2023 18:20","00:05:52","0.40"),
 # --- Main I - evab (continuation) ---
 ("Main I - evab.png","5cb23900ab0dda0001399c94","19 Jun 2023 18:21","00:09:19","0.10"),
 ("Main I - evab.png","612a7980b928fb698777726f","19 Jun 2023 18:21","00:11:42","0.30"),
 ("Main I - evab.png","5f5fd5de4487cd0a1f054104","19 Jun 2023 18:22","00:06:06",""),
 ("Main I - evab.png","5f08f08be711931713bc33f3","19 Jun 2023 18:23","00:15:32","4.30"),
 ("Main I - evab.png","5ccf3006f131fb001706edbb","19 Jun 2023 18:23","00:05:24",""),
 ("Main I - evab.png","60ddb2f00524f416aef58a3e","19 Jun 2023 18:25","00:09:24","0.30"),
 ("Main I - evab.png","609b0969f071a72e09556bf9","19 Jun 2023 18:26","00:08:33",""),
 ("Main I - evab.png","5b2c9b165b5c0900018b45ef","19 Jun 2023 18:27","00:15:21","0.40"),
 ("Main I - evab.png","5e25d8927ea9c201db8a2fd9","19 Jun 2023 18:27","00:14:00","0.30"),
 ("Main I - evab.png","62d6d77df59450e545fb22f6","19 Jun 2023 18:27","00:10:10","4.80"),
 ("Main I - evab.png","60f889d7fd16343c7a36560a","19 Jun 2023 18:29","00:03:32",""),
 ("Main I - evab.png","5ebc1f847fccd102542382fd","19 Jun 2023 18:29","00:03:47","0.10"),
 ("Main I - evab.png","6400c825deb14f9575f7c5ba","19 Jun 2023 18:30","00:08:46","0.30"),
 ("Main I - evab.png","59836c8b06cd1f0001f8e111","19 Jun 2023 18:31","00:07:22",""),
 ("Main I - evab.png","60cfb80f9613ba516472434c","19 Jun 2023 18:31","00:07:56","0.10"),
 ("Main I - evab.png","58cef97d5e07b6000139fa16","19 Jun 2023 18:31","00:05:35","0.30"),
 ("Main I - evab.png","5ac9069f1667e40001d889f2","19 Jun 2023 18:33","00:06:35","4.00"),
 ("Main I - evab.png","6463b4ad932768af9124d41f","19 Jun 2023 18:34","00:07:43","5.00"),
 # --- Main I - eva2 (10) ---
 ("Main I - eva2.png","5ee6d5ce8e523a45fcda497a","19 Jun 2023 19:22","00:04:57","0.30"),
 ("Main I - eva2.png","5f228dd0a6367c7582946207","19 Jun 2023 19:24","00:08:58","0.50"),
 ("Main I - eva2.png","604b4cefcccde3ca319a38b9","19 Jun 2023 19:24","00:06:13","4.10"),
 ("Main I - eva2.png","599c1ec40ed7ae0001991df2","19 Jun 2023 19:28","00:11:38","0.30"),
 ("Main I - eva2.png","595faee2135b5e0001928af8","19 Jun 2023 19:35","00:07:13",""),
 ("Main I - eva2.png","611835b51da9e47cd01c3b03","19 Jun 2023 19:37","00:04:48","0.10"),
 ("Main I - eva2.png","5973c67b5eccd900013a7f8b","19 Jun 2023 19:41","00:10:43","0.40"),
 ("Main I - eva2.png","5f5a07190adc3903dfa338e5","19 Jun 2023 19:42","00:07:50","0.40"),
 ("Main I - eva2.png","5ec107c5a81ee01731ccaebf","19 Jun 2023 19:54","00:05:34",""),
 ("Main I - eva2.png","60f68f4ac13cf8de419f1d8d","19 Jun 2023 19:57","00:11:43","0.30"),
 # --- Main I - eva3 (3) ---
 ("Main I - eva3.png","60d6f0d6545a161dee2fbab0","20 Jun 2023 07:31","00:12:13",""),
 ("Main I - eva3.png","61730961d289d524ad81b49f","20 Jun 2023 07:44","00:08:32","0.80"),
 ("Main I - eva3.png","62fbe4c86d484357b6adbc36","20 Jun 2023 07:47","00:09:26",""),
 # --- Main I - eva4 (3) ---
 ("Main I - eva4.png","5b1ec8d244127b0001400f00","20 Jun 2023 08:23","00:06:18","4.10"),
 ("Main I - eva4.png","59456207b3da5700018450b9","20 Jun 2023 08:28","00:03:04","0.40"),
 ("Main I - eva4.png","5c113e9998e7810001837291","20 Jun 2023 08:39","00:30:23","0.30"),
 # --- Main I - no punish - eva1a (top of 41) ---
 ("Main I - no punish - eva1a.png","58e14a980e54860001ce710a","20 Jun 2023 17:07","00:08:54","0.30"),
 ("Main I - no punish - eva1a.png","5d9d94f373de94001216cbab","20 Jun 2023 17:07","00:08:32",""),
 ("Main I - no punish - eva1a.png","5ef9fa2c7f835a08989f1da8","20 Jun 2023 17:07","00:03:40",""),
 ("Main I - no punish - eva1a.png","59873c08da239a0001fb878f","20 Jun 2023 17:07","00:05:25","0.30"),
 ("Main I - no punish - eva1a.png","611f8186d06a9e1844f3e012","20 Jun 2023 17:08","00:06:46","0.30"),
 ("Main I - no punish - eva1a.png","60e6a9e0dc37b856c7c9ecbf","20 Jun 2023 17:08","00:06:22","0.30"),
 ("Main I - no punish - eva1a.png","5aff493f331e8100018f130d","20 Jun 2023 17:11","00:07:48",""),
 ("Main I - no punish - eva1a.png","613a4439fc2888b3f6b1fc00","20 Jun 2023 17:11","00:07:35","0.30"),
 ("Main I - no punish - eva1a.png","5d31c201c88f0e001a4c3cb3","20 Jun 2023 17:11","00:04:52","4.50"),
 ("Main I - no punish - eva1a.png","5ec9288c8ec8f804d6809d9b","20 Jun 2023 17:12","00:06:59","0.50"),
 ("Main I - no punish - eva1a.png","5da9bb47c19ff3001516bcc3","20 Jun 2023 17:13","00:07:39","0.30"),
 ("Main I - no punish - eva1a.png","6273eeabe7637501530d9733","20 Jun 2023 17:14","00:05:46","0.30"),
 ("Main I - no punish - eva1a.png","5ad0c55ad9f7470001db0e09","20 Jun 2023 17:14","00:06:07","0.30"),
 ("Main I - no punish - eva1a.png","6104d58336ac506a2aa1f325","20 Jun 2023 17:14","00:16:25","4.00"),
 # --- Main I - no punish - eva2 (14) ---
 ("Main I - no punish - eva2.png","605116da9a3b2d13a44665a0","20 Jun 2023 18:16","00:19:17","1.30"),
 ("Main I - no punish - eva2.png","5d049f0e0b54cc0001dad5ba","20 Jun 2023 18:18","00:08:00","1.00"),
 ("Main I - no punish - eva2.png","58456eba000f1000010eb97c","20 Jun 2023 18:19","00:08:34","4.80"),
 ("Main I - no punish - eva2.png","5d1a05e0628de0001966d713","20 Jun 2023 18:21","00:06:46",""),
 ("Main I - no punish - eva2.png","570570eb61ab6a0010d484d0","20 Jun 2023 18:22","00:10:06","0.50"),
 ("Main I - no punish - eva2.png","611588bef241df09a8ac63e1","20 Jun 2023 18:22","00:06:08","4.30"),
 ("Main I - no punish - eva2.png","5e5beb1ed9d6813cae521b50","20 Jun 2023 18:22","00:09:16","0.30"),
 ("Main I - no punish - eva2.png","593081fc5f170a00014358f4","20 Jun 2023 18:23","00:12:57",""),
 ("Main I - no punish - eva2.png","55e9aa1c735c45001043fbb6","20 Jun 2023 18:25","00:06:03",""),
 ("Main I - no punish - eva2.png","5fa8030f008edf5d07a3ab8b","20 Jun 2023 18:26","00:07:20","4.30"),
 ("Main I - no punish - eva2.png","62fb7948bd13412865275d1e","20 Jun 2023 18:26","00:06:36","0.30"),
 ("Main I - no punish - eva2.png","60e80a4d99f424ca5dd14edd","20 Jun 2023 18:28","00:04:57","0.30"),
 ("Main I - no punish - eva2.png","605e7fad494f5b1efc65db99","20 Jun 2023 18:28","00:07:32","4.30"),
 ("Main I - no punish - eva2.png","5a0e9f5c9b760100013a7944","20 Jun 2023 18:28","00:09:48","0.30"),
 # --- Main I - no punish - eva3 (6) ---
 ("Main I - no punish - eva3.png","5de572f21a7af84fc3cd0ca7","20 Jun 2023 18:59","00:07:10","0.30"),
 ("Main I - no punish - eva3.png","60b541217ae30e0573ba59be","20 Jun 2023 18:59","00:07:17","1.30"),
 ("Main I - no punish - eva3.png","5ffcac9fed52b11468dec167","20 Jun 2023 18:59","00:09:37","0.30"),
 ("Main I - no punish - eva3.png","57e131b80cb6700001dd7e5c","20 Jun 2023 19:01","00:06:48","0.30"),
 ("Main I - no punish - eva3.png","5f0c5efb791e025b52cb48b1","20 Jun 2023 19:05","00:08:41","0.30"),
 ("Main I - no punish - eva3.png","63d40b07bb1c70df419c127b","20 Jun 2023 19:05","00:05:34","4.30"),
 # --- Main I - no punish - eva4 (14) ---
 ("Main I - no punish - eva4.png","5bef14ec21057a000140922a","21 Jun 2023 09:11","00:09:29","4.30"),
 ("Main I - no punish - eva4.png","5b9118ad2f7c0c000181e6dc","21 Jun 2023 09:14","00:07:26","0.30"),
 ("Main I - no punish - eva4.png","5f3be0f027d97397cfc8a000","21 Jun 2023 09:16","00:16:50",""),
 ("Main I - no punish - eva4.png","62b234316af4e0c48a6f9073","21 Jun 2023 09:20","00:06:49","4.00"),
 ("Main I - no punish - eva4.png","5e59a78652cf771b84dc6da7","21 Jun 2023 09:24","00:23:55","0.30"),
 ("Main I - no punish - eva4.png","5f0c94983314760efb2814c1","21 Jun 2023 09:25","00:03:38","4.00"),
 ("Main I - no punish - eva4.png","6144d22fe87d4a25b836e37e","21 Jun 2023 09:26","00:06:36","4.30"),
 ("Main I - no punish - eva4.png","5c4f6ecbea0d9a000144b905","21 Jun 2023 09:26","00:05:50","4.00"),
 ("Main I - no punish - eva4.png","5c4499c3d51119000115109a","21 Jun 2023 09:26","00:08:35",""),
 ("Main I - no punish - eva4.png","5d593dbaa0c0940001a471be","21 Jun 2023 09:27","00:06:45","4.00"),
 ("Main I - no punish - eva4.png","5f70f2db1da187103ac30229","21 Jun 2023 09:30","00:06:34",""),
 ("Main I - no punish - eva4.png","5b424267e8815c0001777d94","21 Jun 2023 09:31","00:11:48","0.30"),
 ("Main I - no punish - eva4.png","5d61b636d989a4001a236c0e","21 Jun 2023 09:33","00:01:52","4.00"),
 ("Main I - no punish - eva4.png","5ee0c8a669a88041d4034cea","21 Jun 2023 09:33","00:06:21","4.00"),
 # --- Main I - no punish - eva5 (7) ---
 ("Main I - no punish - eva5.png","61673b692a55fba0f6b8abf1","21 Jun 2023 10:09","00:08:11","0.30"),
 ("Main I - no punish - eva5.png","5e3d33b27525e7117bd31778","21 Jun 2023 10:11","00:08:47",""),
 ("Main I - no punish - eva5.png","5cc18045796f460019034fba","21 Jun 2023 10:11","00:10:19","4.00"),
 ("Main I - no punish - eva5.png","631772a21801f95e886518f4","21 Jun 2023 10:11","00:03:45","0.50"),
 ("Main I - no punish - eva5.png","63e3c4bb98ef1111f6026e28","21 Jun 2023 10:12","00:07:10","4.00"),
 ("Main I - no punish - eva5.png","5f02e4ccf8b6db18a3a60ccd","21 Jun 2023 10:26","00:04:32",""),
 ("Main I - no punish - eva5.png","5fb274f5557bcc848df4293a","21 Jun 2023 10:26","00:09:21",""),
]

# Build candidate sets per pdf
pdf_cache = {}
def candidates(png):
    pdf = STUDY_PDF.get(png)
    if not pdf: return []
    if pdf not in pdf_cache: pdf_cache[pdf] = pdf_ids(pdf)
    return pdf_cache[pdf]

rows_out = []
used = {}  # pdf -> set(matched ids)
for png, ocr, started, tt, bonus in RAW:
    cands = candidates(png)
    m = difflib.get_close_matches(ocr, cands, n=1, cutoff=0.55) if cands else []
    if m:
        pid, src = m[0], ("exact" if m[0]==ocr else "pdf_corrected")
        pdf = STUDY_PDF[png]; used.setdefault(pdf,set()).add(pid)
    else:
        pid, src = ocr, "ocr_only"
    rows_out.append((pid, started, tt, bonus, png, src))

with open(os.path.join(HERE,"submissions_digitized.csv"),"w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["prolific_id","started","time_taken","bonus","png_file","id_source"])
    w.writerows(rows_out)

# Report
from collections import Counter
print("rows written:", len(rows_out))
print("id_source:", dict(Counter(r[5] for r in rows_out)))
print("\nPer study: matched vs PDF-approved count")
for pdf in sorted(set(STUDY_PDF.values())):
    total = len(pdf_cache.get(pdf, pdf_ids(pdf)))
    got = len(used.get(pdf,set()))
    flag = "" if got==total else "   <-- MISSING %d (low-res continuation)"%(total-got)
    print(f"  {got:>2}/{total:<2}  {pdf}{flag}")

# List the participants whose metrics are missing (only in low-res delb / eva1b)
for pdf in ["Main I - del.pdf","Main I - no punish - eva1.pdf"]:
    allids = set(pdf_cache.get(pdf, pdf_ids(pdf)))
    missing = sorted(allids - used.get(pdf,set()))
    print(f"\nMISSING metrics ({pdf}, need re-export of the low-res image) -- {len(missing)} ids:")
    for i in missing: print("   ", i)
