import random
cnc_sign={"cnk_1":0,"cnk_2":0,"cnk_3":0,"cnk_4":0,"cnk_5":0,"cnk_6":0,"cnk_7":0,"cnk_8":0}
cnc_set={"cnk_1":1,"cnk_2":1,"cnk_3":2,"cnk_4":2,"cnk_5":3,"cnk_6":3,"cnk_7":4,"cnk_8":4}
cnc_time={"cnk_1":0,"cnk_2":0,"cnk_3":0,"cnk_4":0,"cnk_5":0,"cnk_6":0,"cnk_7":0,"cnk_8":0}
rgv_set=1
total_time=0
rgv_move1=23
rgv_move2=41
rgv_move3=59
cnc_one=580
cnc_two_one=400
cnc_two_two=378
rgv_ji=30
rgv_ou=35
rgv_clear=30
work=0
rgv_time=0
wl_time=0
aim=False
aim_wl=False
aim_made=False
stop=False
clear=0
ok=False
huai={"cnk_1":0,"cnk_2":0,"cnk_3":0,"cnk_4":0,"cnk_5":0,"cnk_6":0,"cnk_7":0,"cnk_8":0}
huai_time={"cnk_1":0,"cnk_2":0,"cnk_3":0,"cnk_4":0,"cnk_5":0,"cnk_6":0,"cnk_7":0,"cnk_8":0}
rand_tag=False

wl={"cnk_1":0,"cnk_2":0,"cnk_3":0,"cnk_4":0,"cnk_5":0,"cnk_6":0,"cnk_7":0,"cnk_8":0}
def inp():
    try:
        global rgv_move1
        global rgv_move2
        global rgv_move3
        global cnc_one
        global rgv_ji
        global rgv_ou
        global rgv_clear
        rgv_move1=eval(input("RGV移动1个单位所需时间"))
        rgv_move2=eval(input("RGV移动2个单位所需时间"))
        rgv_move3=eval(input("RGV移动3个单位所需时间"))
        cnc_one=eval(input("CNC加工完成一个一道工序的物料所需时间"))
        rgv_ji=eval(input("RGV为CNC1#，3#，5#，7#一次上下料所需时间"))
        rgv_ou=eval(input("RGV为CNC2#，4#，6#，8#一次上下料所需时间"))
        rgv_clear=eval(input("RGV完成一个物料的清洗作业所需时间"))
    except:
        print("输入有误")
        inp()
inp()

while True:
    if total_time>=8*60*60:
        print("8小时完成数：{}".format(work))
        break
    else:

        for i in cnc_sign:
            if wl[i]==1:
                a=random.randint(1,100*cnc_one)
                if a==10:
                    huai[i]=1
                if total_time-cnc_time[i]>=cnc_one and huai[i]==0:
                    aim_made=True
                    if aim_made==True:
                        clear=total_time
                        while  total_time-clear<rgv_clear:
                               total_time+=1
                               ok=True
                        if ok==True and total_time-clear==rgv_clear:
                               work+=1
                               aim=False
                               wl[i]=0
                               cnc_sign[i]=0
                elif huai[i]==1:
                    huai_time[i]=total_time
                    if rand_tag==False:
                        last_huai=random.randint(10*60,20*60)
                        rand_tag=True
                    if total_time-huai_time[i]>=last_huai:
                        wl[i]=0
                        cnc_sign[i]=0
                        aim=False
                        huai[i]=0
                        rand_tag=False

            if cnc_sign[i]==0 :
                cnc_sign[i]=1
                if abs(cnc_set[i]-rgv_set)==1:
                    rgv_time=total_time
                    while total_time-rgv_time<rgv_move1:
                        total_time+=1
                        rgv_set=cnc_set[i]
                        cnc_sign[i]=1
                        ok=True
                    if total_time-rgv_time==rgv_move1 and ok==True:
                        ok= False
                        aim=True
                    if aim==True:
                            if i in "cnk_1 cnk_3 cnk_5 cnk_7" :
                                 if wl[i]==0:
                                     wl_time=total_time
                                     while total_time-wl_time<rgv_ji:
                                            total_time+=1
                                            ok=True
                                     if ok==True and total_time-wl_time==rgv_ji:
                                            aim_wl=True
                                            ok=False
                                            wl[i]=1
                                 if aim_wl==True:
                                            aim_wl=False
                                            cnc_time[i]=total_time
                            else:
                                 if wl[i]==0:
                                     wl_time=total_time
                                     while total_time-wl_time<rgv_ou:
                                            total_time+=1
                                            ok=True
                                     if ok==True and total_time-wl_time==rgv_ou:
                                            aim_wl=True
                                            ok=False
                                            wl[i]=1
                                 if aim_wl==True:
                                            aim_wl=False
                                            cnc_time[i]=total_time
                elif abs(cnc_set[i]-rgv_set)==2:
                    rgv_time=total_time
                    while total_time-rgv_time<rgv_move2:
                        total_time+=1
                        rgv_set=cnc_set[i]
                        cnc_sign[i]=1
                        ok=True
                    if total_time-rgv_time==rgv_move2 and ok==True:
                        ok= False
                        aim=True
                    if aim==True:
                            if i in "cnk_1 cnk_3 cnk_5 cnk_7" :
                                 if wl[i]==0:
                                     wl_time=total_time
                                     while total_time-wl_time<rgv_ji:
                                            total_time+=1
                                            ok=True
                                     if ok==True and total_time-wl_time==rgv_ji:
                                            aim_wl=True
                                            ok=False
                                            wl[i]=1
                                 if aim_wl==True:
                                            aim_wl=False
                                            cnc_time[i]=total_time
                            else:
                                 if wl[i]==0:
                                     wl_time=total_time
                                     while total_time-wl_time<rgv_ou:
                                            total_time+=1
                                            ok=True
                                     if ok==True and total_time-wl_time==rgv_ou:
                                            aim_wl=True
                                            ok=False
                                            wl[i]=1
                                 if aim_wl==True:
                                            aim_wl=False
                                            cnc_time[i]=total_time
                elif  abs(cnc_set[i]-rgv_set)==3:
                    rgv_time=total_time
                    while total_time-rgv_time<rgv_move3:
                        total_time+=1
                        rgv_set=cnc_set[i]
                        cnc_sign[i]=1
                        ok=True
                    if total_time-rgv_time==rgv_move3 and ok==True:
                        ok= False
                        aim=True
                    if aim==True:
                            if i in "cnk_1 cnk_3 cnk_5 cnk_7" :
                                 if wl[i]==0:
                                     wl_time=total_time
                                     while total_time-wl_time<rgv_ji:
                                            total_time+=1
                                            ok=True
                                     if ok==True and total_time-wl_time==rgv_ji:
                                            aim_wl=True
                                            ok=False
                                            wl[i]=1
                                 if aim_wl==True:
                                            aim_wl=False
                                            cnc_time[i]=total_time
                            else:
                                 if wl[i]==0:
                                     wl_time=total_time
                                     while total_time-wl_time<rgv_ou:
                                            total_time+=1
                                            ok=True
                                     if ok==True and total_time-wl_time==rgv_ou:
                                            aim_wl=True
                                            ok=False
                                            wl[i]=1
                                 if aim_wl==True:
                                            aim_wl=False
                                            cnc_time[i]=total_time
                elif  abs(cnc_set[i]-rgv_set)==0:
                    ok= False
                    aim=True
                    if aim==True:
                            if i in "cnk_1 cnk_3 cnk_5 cnk_7" :
                                 if wl[i]==0:
                                     wl_time=total_time
                                     while total_time-wl_time<rgv_ji:
                                            total_time+=1
                                            ok=True
                                     if ok==True and total_time-wl_time==rgv_ji:
                                            aim_wl=True
                                            ok=False
                                            wl[i]=1
                                 if aim_wl==True:
                                            aim_wl=False
                                            cnc_time[i]=total_time
                            else:
                                 if wl[i]==0:
                                     wl_time=total_time
                                     while total_time-wl_time<rgv_ou:
                                            total_time+=1
                                            ok=True
                                     if ok==True and total_time-wl_time==rgv_ou:
                                            aim_wl=True
                                            ok=False
                                            wl[i]=1
                                 if aim_wl==True:
                                            aim_wl=False
                                            cnc_time[i]=total_time
        total_time+=1
