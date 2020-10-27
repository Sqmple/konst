from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
button_1 = types.InlineKeyboardButton("Биология", callback_data='biology')
button_2 = types.InlineKeyboardButton("География", callback_data='geography')
button_3 = types.InlineKeyboardButton("Английский язык", callback_data='english')
button_4 = types.InlineKeyboardButton("Математика", callback_data='math')
button_5 = types.InlineKeyboardButton("Украинская литература", callback_data='ukraine literature')
button_6 = types.InlineKeyboardButton("Украинский язык", callback_data='ukraine language')
button_7 = types.InlineKeyboardButton("Физика", callback_data='physics')
button_8 = types.InlineKeyboardButton("Химия", callback_data='chemistry')
button = types.InlineKeyboardMarkup().add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8)
# 1 страница
bt_1 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back')
bt_2 = types.InlineKeyboardButton("2-я страница", callback_data='knost')
bt = types.InlineKeyboardMarkup().add(bt_1, bt_2)
# кнопка для перехода на страницу 2 (конспекта по биологию)
bt_3 = types.InlineKeyboardButton("Назад на 1 страницу", callback_data='lorst')
bt_4 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_2')
bt_5 = types.InlineKeyboardButton("3-я страница", callback_data='konsp_3')
bg = types.InlineKeyboardMarkup().add(bt_3, bt_4, bt_5)
# кнопка для перехода на страницу 3 (конспекта по биологию)
vb_1 = types.InlineKeyboardButton("Назад на 2-я", callback_data='fg')
vb_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_3')
vb_3 = types.InlineKeyboardButton("4-я страница", callback_data='fg_2')
vb = types.InlineKeyboardMarkup().add(vb_1, vb_2, vb_3)
# кнопка для перехода на страницу 4 (конспекта по биологию)
vd_1 = types.InlineKeyboardButton("Назад на 3-я ", callback_data='fg_3')
vd_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_4')
vd_3 = types.InlineKeyboardButton("5-я страница", callback_data='fg_4')
vd = types.InlineKeyboardMarkup().add(vd_1, vd_2, vd_3)
# кнопка для перехода на страницу 5 (конспекта по биологию)
vg_1 = types.InlineKeyboardButton("Назад на 4 страницу ", callback_data='fg_5')
vg_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_5')
vg_3 = types.InlineKeyboardButton("6-я страница", callback_data='fg_6')
vg = types.InlineKeyboardMarkup().add(vg_1, vg_2, vg_3)
# кнопка для перехода на страницу 6 (конспекта по биологию)
vh_1 = types.InlineKeyboardButton("Назад на 5 страницу", callback_data='fg_7')
vh_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_6')
vh_3 = types.InlineKeyboardButton("7-я страница", callback_data='fg_8')
vh = types.InlineKeyboardMarkup().add(vh_1, vh_2, vh_3)
# кнопка для перехода на страницу 7 (конспекта по биологию)
vl_1 = types.InlineKeyboardButton("Назад на 6 страницу ", callback_data='fg_9')
vl_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_7')
vl_3 = types.InlineKeyboardButton("8-я страница", callback_data='fg_10')
vl = types.InlineKeyboardMarkup().add(vl_1, vl_2, vl_3)
# кнопка для перехода на страницу 8 (конспекта по биологию)
vk_1 = types.InlineKeyboardButton("Назад на 7 страницу", callback_data='fg_11')
vk_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_8')
vk_3 = types.InlineKeyboardButton("9-я страница", callback_data='fg_12')
vk = types.InlineKeyboardMarkup().add(vk_1, vk_2, vk_3)
# кнопка для перехода на страницу 9 (конспекта по биологию)
vkl_1 = types.InlineKeyboardButton("Назад на 8 страницу", callback_data='fg_13')
vkl_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_9')
vkl_3 = types.InlineKeyboardButton("10-я страница", callback_data='fg_14')
vkl = types.InlineKeyboardMarkup().add(vkl_1, vkl_2, vkl_3)
# кнопка для перехода на страницу 10 (конспекта по биологию)
vgl_1 = types.InlineKeyboardButton("Назад на 9 страницу", callback_data='fg_15')
vgl_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_10')
vgl_3 = types.InlineKeyboardButton("11-я страница", callback_data='fg_16')
vgl = types.InlineKeyboardMarkup().add(vgl_1, vgl_2, vgl_3)
# кнопка для перехода на страницу 11 (конспекта по биологию)
sgl_1 = types.InlineKeyboardButton("Назад на 10 страницу", callback_data='fg_17')
sgl_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_11')
sgl_3 = types.InlineKeyboardButton("12-я страница", callback_data='fg_18')
sgl = types.InlineKeyboardMarkup().add(sgl_1, sgl_2, sgl_3)
# кнопка для перехода на страницу 12 (конспекта по биологию)
sgs_1 = types.InlineKeyboardButton("Назад на 11 страницу", callback_data='fg_19')
sgs_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_12')
sgs_3 = types.InlineKeyboardButton("13-я страница", callback_data='fg_20')
sgs = types.InlineKeyboardMarkup().add(sgs_1, sgs_2, sgs_3)
# кнопка для перехода на страницу 13 (конспекта по биологию)
sds_1 = types.InlineKeyboardButton("Назад на 12 страницу", callback_data='fg_21')
sds_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_13')
sds_3 = types.InlineKeyboardButton("14-я страница", callback_data='fg_22')
sds = types.InlineKeyboardMarkup().add(sds_1, sds_2, sds_3)
# кнопка для перехода на страницу 14 (конспекта по биологию)
sdz_1 = types.InlineKeyboardButton("Назад на 13 страницу", callback_data='fg_23')
sdz_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_14')
sdz_3 = types.InlineKeyboardButton("15-я страница", callback_data='fg_24')
sdz = types.InlineKeyboardMarkup().add(sdz_1, sdz_2, sdz_3)
# кнопка для перехода на страницу 15 (конспекта по биологию)
adz_1 = types.InlineKeyboardButton("Назад на 14 страницу", callback_data='fg_25')
adz_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_15')
adz_3 = types.InlineKeyboardButton("16-я страница", callback_data='fg_26')
adz = types.InlineKeyboardMarkup().add(adz_1, adz_2, adz_3)
# кнопка для перехода на страницу 16 (конспекта по биологию)
bdz_1 = types.InlineKeyboardButton("Назад на 15 страницу", callback_data='fg_27')
bdz_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_16')
bdz_3 = types.InlineKeyboardButton("17-я страница", callback_data='fg_28')
bdz = types.InlineKeyboardMarkup().add(bdz_1, bdz_2, bdz_3)
# кнопка для перехода на страницу 17 (конспекта по биологию)
cdz_1 = types.InlineKeyboardButton("Назад на 16 страницу", callback_data='fg_29')
cdz_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_17')
cdz_3 = types.InlineKeyboardButton("18-я страница", callback_data='fg_30')
cdz = types.InlineKeyboardMarkup().add(cdz_1, cdz_2, cdz_3)
# кнопка для перехода на страницу 18 (конспекта по биологию)
mdz_1 = types.InlineKeyboardButton("Назад на 17 страницу", callback_data='fg_31')
mdz_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_18')
mdz_3 = types.InlineKeyboardButton("19-я страница", callback_data='fg_32')
mdz = types.InlineKeyboardMarkup().add(mdz_1, mdz_2, mdz_3)
# кнопка для перехода на страницу 19 (конспекта по биологию)
cmz_1 = types.InlineKeyboardButton("Назад на 18 страницу", callback_data='fg_33')
cmz_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_19')
cmz_3 = types.InlineKeyboardButton("20-я страница", callback_data='fg_34')
cmz = types.InlineKeyboardMarkup().add(cmz_1, cmz_2, cmz_3)
# кнопка для перехода на страницу 20 (конспекта по биологию)
zdz_1 = types.InlineKeyboardButton("Назад на 19 страницу", callback_data='fg_35')
zdz_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_20')
zdz_3 = types.InlineKeyboardButton("21-я страница", callback_data='fg_36')
zdz = types.InlineKeyboardMarkup().add(zdz_1, zdz_2, zdz_3)
# кнопка для перехода на страницу 21 (конспекта по биологию)
ydz_1 = types.InlineKeyboardButton("Назад на 20 страницу", callback_data='fg_37')
ydz_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_21')
ydz_3 = types.InlineKeyboardButton("22-я страница", callback_data='fg_38')
ydz = types.InlineKeyboardMarkup().add(ydz_1, ydz_2, ydz_3)
# кнопка для перехода на страницу 22 (конспекта по биологию)
gdz_1 = types.InlineKeyboardButton("Назад на 21 страницу", callback_data='fg_39')
gdz_2 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='back_22')
gdz_3 = types.InlineKeyboardButton("23-я страница", callback_data='fg_40')
gdz = types.InlineKeyboardMarkup().add(gdz_1, gdz_2, gdz_3)

# География
geo_1 = types.InlineKeyboardButton("Главное меню", callback_data='main')
geo_2 = types.InlineKeyboardButton("2-я страница", callback_data='photo')
geo = types.InlineKeyboardMarkup().add(geo_1, geo_2)
# кнопка для перехода на 2 страницу
geo_3 = types.InlineKeyboardButton("Главное меню", callback_data='main_2')
geo_4 = types.InlineKeyboardButton("Назад на 1 страницу", callback_data='laf')
geo_5 = types.InlineKeyboardButton("3-я страница", callback_data='photo_2')
geo_1 = types.InlineKeyboardMarkup().add(geo_3, geo_4, geo_5)
# кнопка для перехода на 3 страницу
geo_6 = types.InlineKeyboardButton("Главное меню", callback_data='main_3')
geo_7 = types.InlineKeyboardButton("Назад на 2 страницу", callback_data='laf_2')
geo_8 = types.InlineKeyboardButton("4-я страница", callback_data='photo_3')
geo_2 = types.InlineKeyboardMarkup().add(geo_6, geo_7, geo_8)
# кнопка для перехода на 4 страницу
geo_9 = types.InlineKeyboardButton("Главное меню", callback_data='main_4')
geo_10 = types.InlineKeyboardButton("Назад на 3 страницу", callback_data='laf_3')
geo_11 = types.InlineKeyboardButton("5-я страница", callback_data='photo_4')
geo_3 = types.InlineKeyboardMarkup().add(geo_9, geo_10, geo_11)
# кнопка для перехода на 5 страницу
gh = types.InlineKeyboardButton("Главное меню", callback_data='main_5')
gh_1 = types.InlineKeyboardButton("Назад на 4 страницу", callback_data='laf_4')
gh_2 = types.InlineKeyboardButton("6-я страница", callback_data='photo_5')
gh_3 = types.InlineKeyboardMarkup().add(gh, gh_1, gh_2)

# кнопка для перехода на 6 страницу
gl = types.InlineKeyboardButton("Главное меню", callback_data='main_6')
gl_1 = types.InlineKeyboardButton("Назад на 5 страницу", callback_data='laf_5')
gl_2 = types.InlineKeyboardButton("7-я страница", callback_data='photo_6')
gl_3 = types.InlineKeyboardMarkup().add(gl, gl_1, gl_2)

# кнопка для перехода на 7 страницу
gd_1 = types.InlineKeyboardButton("Главное меню", callback_data='main_7')
gd_2 = types.InlineKeyboardButton("Назад на 6 страницу", callback_data='laf_6')
gd_3 = types.InlineKeyboardButton("8-я страница", callback_data='photo_7')
gd = types.InlineKeyboardMarkup().add(gd_1, gd_2, gd_3)
# кнопка для перехода на 8 страницу
gb_1 = types.InlineKeyboardButton("Главное меню", callback_data='main_8')
gb_2 = types.InlineKeyboardButton("Назад на 7 страницу", callback_data='laf_7')
gb_3 = types.InlineKeyboardButton("9-я страница", callback_data='photo_8')
gb = types.InlineKeyboardMarkup().add(gb_1, gb_2, gb_3)
# кнопка для перехода на 9 страницу
gbd_1 = types.InlineKeyboardButton("Главное меню", callback_data='main_9')
gbd_2 = types.InlineKeyboardButton("Назад на 8 страницу", callback_data='laf_8')
gbd_3 = types.InlineKeyboardButton("10-я страница", callback_data='photo_9')
gbd = types.InlineKeyboardMarkup().add(gbd_1, gbd_2, gbd_3)
# кнопка для перехода на 10 страницу
gld_1 = types.InlineKeyboardButton("Главное меню", callback_data='main_10')
gld_2 = types.InlineKeyboardButton("Назад на 9 страницу", callback_data='laf_9')
gld_3 = types.InlineKeyboardButton("11-я страница", callback_data='photo_10')
gld = types.InlineKeyboardMarkup().add(gld_1, gld_2, gld_3)

# Английский 2 кнопки одно словарь,вторая конспекты

english_1 = types.InlineKeyboardButton("Словарь", callback_data='words')
english_2 = types.InlineKeyboardButton("Конспект", callback_data='konsp_english')
eng_main = types.InlineKeyboardMarkup().add(english_1, english_2)

# словарь
word_1 = types.InlineKeyboardButton("Главное меню", callback_data='main_menu')
word_2 = types.InlineKeyboardButton("2-я страница", callback_data='2_search')
word = types.InlineKeyboardMarkup().add(word_1, word_2)

# кнопка для перехода на 2 страницу
wor_1 = types.InlineKeyboardButton("Главное меню", callback_data='main_m')
wor_2 = types.InlineKeyboardButton("Назад на 1 страницу", callback_data='kgw')
wor_3 = types.InlineKeyboardButton('3-я страница', callback_data='phot')
wor = types.InlineKeyboardMarkup().add(wor_1, wor_2, wor_3)

# кнопка для перехода на 3 страницу
lor_1 = types.InlineKeyboardButton("Главное меню", callback_data='lrgk')
lor_2 = types.InlineKeyboardButton("Назад на 2 страницу", callback_data='mvg')
lor_3 = types.InlineKeyboardButton('4-я страница', callback_data='vfg')
lor = types.InlineKeyboardMarkup().add(lor_1, lor_2, lor_3)