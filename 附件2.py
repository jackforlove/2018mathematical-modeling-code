import random
cnc_sign={"cnk_1":0,"cnk_3":0,"cnk_5":0,"cnk_7":0,"cnk_2":0,"cnk_4":0,"cnk_6":0,"cnk_8":0}
cnc_set={"cnk_1":1,"cnk_3":2,"cnk_5":3,"cnk_7":4,"cnk_2":1,"cnk_4":2,"cnk_6":3,"cnk_8":4}
cnc_time={"cnk_1":0,"cnk_3":0,"cnk_5":0,"cnk_7":0,"cnk_2":0,"cnk_4":0,"cnk_6":0,"cnk_8":0}
rgv_set=1
total_time=0
rgv_move1=23
rgv_move2=41
rgv_move3=59
cnc_one=580
cnc_two_one=280
cnc_two_two=500
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
huai={"cnk_1":0,"cnk_3":0,"cnk_5":0,"cnk_7":0,"cnk_2":0,"cnk_4":0,"cnk_6":0,"cnk_8":0}
huai_time={"cnk_1":0,"cnk_3":0,"cnk_5":0,"cnk_7":0,"cnk_2":0,"cnk_4":0,"cnk_6":0,"cnk_8":0}
rand_tag=False
wl={"cnk_1":0,"cnk_3":0,"cnk_5":0,"cnk_7":0,"cnk_2":0,"cnk_4":0,"cnk_6":0,"cnk_8":0}
finish={"cnk_1":0,"cnk_3":0,"cnk_5":0,"cnk_7":0,"cnk_2":0,"cnk_4":0,"cnk_6":0,"cnk_8":0}
gongxu={"cnk_1":0,"cnk_3":0,"cnk_5":0,"cnk_7":0,"cnk_2":0,"cnk_4":0,"cnk_6":0,"cnk_8":0}
keep=""
lock=False
jmp=False
def inp():
    try:
        global rgv_move1
        global rgv_move2
        global rgv_move3
        global rgv_clear
        global cnc_one
        global cnc_two_one
        global cnc_two_two
        global rgv_clear
        global rgv_ji
        global rgv_ou
        rgv_move1=eval(input("RGV移动1个单位所需时间"))
        rgv_move2=eval(input("RGV移动2个单位所需时间"))
        rgv_move3=eval(input("RGV移动3个单位所需时间"))
        cnc_one=eval(input("CNC加工完成一个一道工序的物料所需时间"))
        cnc_two_one=eval(input("CNC加工完成一个两道工序物料的第一道工序所需时间"))
        cnc_two_two=eval(input("CNC加工完成一个两道工序物料的第二道工序所需时间"))
        rgv_ji=eval(input("RGV为CNC1#，3#，5#，7#一次上下料所需时间"))
        rgv_ou=eval(input("RGV为CNC2#，4#，6#，8#一次上下料所需时间"))
        rgv_clear=eval(input("RGV完成一个物料的清洗作业所需时间"))
    except:
        print("输入有误")
        inp()
inp()
A=round(cnc_two_one*(8/(cnc_two_one+cnc_two_two)))
B=round(cnc_two_two*(8/(cnc_two_one+cnc_two_two)))
while True:
    if total_time>=8*60*60:
        print("8小时完成数：{}".format(work))
        break
    else:
        for i in cnc_sign:
            if jmp==True:
                jmp=False
                break
            if wl[i]==1:
                if total_time-cnc_time[i]>=cnc_two_one and huai[i]==0 and gongxu[i]==0:
                    aim_made=True
                    finish[i]=1

            if cnc_sign[i]==0 :
                if gongxu[i]==0 and i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[:A*5] and lock==False:
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
                                if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[:A*5] :
                                     if wl[i]==0:
                                         wl_time=total_time
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 print("{}时{}分{}秒".format(m[0],m[1],n[1]),i)
                                             else:
                                                 print("{}分{}秒".format(n[0],n[1]),i)
                                         else:
                                             print("{}秒".format(wl_time),i)
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
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 # print("{}时{}分{}秒".format(m[0],m[1],n[1]),i)
                                             else:
                                                 pass# print("{}分{}秒".format(n[0],n[1],n[0],n[1]+rgv_ou),i)
                                         else:
                                             pass# print("{}秒".format(wl_time),i)
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
                                if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[:A*5] :
                                     if wl[i]==0:
                                         wl_time=total_time
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 print("{}时{}分{}秒".format(m[0],m[1],n[1]),i)
                                             else:
                                                 print("{}分{}秒".format(n[0],n[1]),i)
                                         else:
                                             print("{}秒".format(wl_time),i)
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
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 # print("{}时{}分{}秒".format(m[0],m[1],n[1]),i)
                                             else:
                                                 pass# print("{}分{}秒".format(n[0],n[1]),i)
                                         else:
                                             pass# print("{}秒".format(wl_time),i)
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
                                if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[:A*5] :
                                     if wl[i]==0:
                                         wl_time=total_time
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 print("{}时{}分{}秒".format(m[0],m[1],n[1]),i)
                                             else:
                                                 print("{}分{}秒".format(n[0],n[1]),i)
                                         else:
                                             print("{}秒".format(wl_time),i)
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
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 # print("{}时{}分{}秒".format(m[0],m[1],n[1]),i)
                                             else:
                                                 pass# print("{}分{}秒".format(n[0],n[1]),i)
                                         else:
                                             pass# print("{}秒".format(wl_time),i)
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
                                if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[:A*5] :
                                     if wl[i]==0:
                                         wl_time=total_time
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 print("{}时{}分{}秒".format(m[0],m[1],n[1]),i)
                                             else:
                                                 print("{}分{}秒".format(n[0],n[1]),i)
                                         else:
                                             print("{}秒".format(wl_time),i)
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
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 # print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                             else:
                                                 pass# print("{}分{}秒".format(n[0],n[1]))
                                         else:
                                             pass# print("{}秒".format(wl_time))
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
                elif lock==True:
                        if abs(cnc_set[i]-rgv_set)==1:
                            if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[A*5:] :
                                    if wl[i]==0:
                                        rgv_time=total_time
                                        while total_time-rgv_time<rgv_move1:
                                            total_time+=1
                                            rgv_set=cnc_set[i]
                                            ok=True
                                        if total_time-rgv_time==rgv_move1 and ok==True:
                                            ok= False
                                            aim=True
                                        if aim==True:
                                             wl_time=total_time
                                             if wl_time>=60:
                                                 n=divmod(wl_time,60)
                                                 if n[0]>=60:
                                                     m=divmod(n[0],60)
                                                     # print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                                 else:

                                                     pass# print("{}分{}秒".format(n[0],n[1]))
                                             else:

                                                 pass# print("{}秒".format(wl_time))
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
                                                        cnc_sign[i]=1
                                                        lock=False
                                                        gongxu[keep]=0
                                                        keep=""
                                                        jmp=True
                        elif abs(cnc_set[i]-rgv_set)==2:
                            if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[A*5:] :
                                    if wl[i]==0:
                                        rgv_time=total_time
                                        while total_time-rgv_time<rgv_move1:
                                            total_time+=1
                                            rgv_set=cnc_set[i]
                                            ok=True
                                        if total_time-rgv_time==rgv_move1 and ok==True:
                                            ok= False
                                            aim=True
                                        if aim==True:
                                             wl_time=total_time
                                             if wl_time>=60:
                                                 n=divmod(wl_time,60)
                                                 if n[0]>=60:
                                                     m=divmod(n[0],60)

                                                     # print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                                 else:

                                                     pass# print("{}分{}秒".format(n[0],n[1]))
                                             else:

                                                 pass# print("{}秒".format(wl_time))
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
                                                        cnc_sign[i]=1
                                                        lock=False
                                                        gongxu[keep]=0
                                                        keep=""
                                                        jmp=True
                        elif  abs(cnc_set[i]-rgv_set)==3:
                            if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[A*5:] :
                                    if wl[i]==0:
                                        rgv_time=total_time
                                        while total_time-rgv_time<rgv_move1:
                                            total_time+=1
                                            rgv_set=cnc_set[i]
                                            ok=True
                                        if total_time-rgv_time==rgv_move1 and ok==True:
                                            ok= False
                                            aim=True
                                        if aim==True:
                                             wl_time=total_time
                                             if wl_time>=60:
                                                 n=divmod(wl_time,60)
                                                 if n[0]>=60:
                                                     m=divmod(n[0],60)
                                                     pass# print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                                 else:

                                                     pass# print("{}分{}秒".format(n[0],n[1]))
                                             else:

                                                 pass# print("{}秒".format(wl_time))
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
                                                        cnc_sign[i]=1
                                                        gongxu[keep]=0
                                                        keep=""
                                                        lock=False
                                                        jmp=True
                        elif  abs(cnc_set[i]-rgv_set)==0:
                            ok= False
                            aim=True
                            if aim==True:
                                   if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[A*5:] :
                                    if wl[i]==0:
                                        rgv_time=total_time
                                        while total_time-rgv_time<rgv_move1:
                                            total_time+=1
                                            rgv_set=cnc_set[i]
                                            ok=True
                                        if total_time-rgv_time==rgv_move1 and ok==True:
                                            ok= False
                                            aim=True
                                        if aim==True:
                                             wl_time=total_time
                                             if wl_time>=60:
                                                 n=divmod(wl_time,60)
                                                 if n[0]>=60:
                                                     m=divmod(n[0],60)
                                                     # print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                                 else:
                                                     pass
                                                     # print("{}分{}秒".format(n[0],n[1]))
                                             else:
                                                 pass
                                                 # print("{}秒".format(wl_time))
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
                                                        cnc_sign[i]=1
                                                        gongxu[keep]=0
                                                        keep=""
                                                        lock=False
                                                        jmp=True
            elif finish[i]==1 and lock==False:
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
                            if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[:A*5] :
                                if gongxu[i]==0:
                                    if wl[i]==1:
                                         wl_time=total_time
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                             else:
                                                 print("{}分{}秒".format(n[0],n[1]))
                                         else:
                                             print("{}秒".format(wl_time))
                                         while total_time-wl_time<rgv_ji:
                                                total_time+=1
                                                ok=True
                                         if ok==True and total_time-wl_time==rgv_ji:
                                                aim_wl=False
                                                gongxu[i]=1
                                                keep=i
                                                lock=True
                                                # print("一道工序完成",i)
                                                ok=False
                                                wl[i]=1
                                                aim=False
                                                finish[i]=0
                                                cnc_time[i]=total_time
                                                cnc_sign[i]=1
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
                            if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[:A*5] :
                                if gongxu[i]==0:
                                    if wl[i]==1:
                                         wl_time=total_time
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                             else:
                                                 print("{}分{}秒".format(n[0],n[1]))
                                         else:
                                             print("{}秒".format(wl_time))
                                         while total_time-wl_time<rgv_ji:
                                                total_time+=1
                                                ok=True
                                         if ok==True and total_time-wl_time==rgv_ji:
                                                aim_wl=False
                                                gongxu[i]=1
                                                keep=i
                                                lock=True
                                                # print("一道工序完成",i)
                                                ok=False
                                                wl[i]=1
                                                aim=False
                                                finish[i]=0
                                                cnc_time[i]=total_time
                                                cnc_sign[i]=1

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
                            if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[:A*5] :
                                if gongxu[i]==0:
                                    if wl[i]==1:
                                         wl_time=total_time
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                             else:
                                                 print("{}分{}秒".format(n[0],n[1]))
                                         else:
                                             print("{}秒".format(wl_time))
                                         while total_time-wl_time<rgv_ji:
                                                total_time+=1
                                                ok=True
                                         if ok==True and total_time-wl_time==rgv_ji:
                                                aim_wl=False
                                                gongxu[i]=1
                                                keep=i
                                                lock=True
                                                # print("一道工序完成",i)
                                                ok=False
                                                wl[i]=1
                                                aim=False
                                                finish[i]=0
                                                cnc_time[i]=total_time
                                                cnc_sign[i]=1

                elif  abs(cnc_set[i]-rgv_set)==0:
                    ok= False
                    aim=True
                    if aim==True:
                            if i in "cnk_1cnk_3cnk_5cnk_7cnk_2cnk_4cnk_6cnk_8"[:A*5] :
                                if gongxu[i]==0:
                                    if wl[i]==1:
                                         wl_time=total_time
                                         if wl_time>=60:
                                             n=divmod(wl_time,60)
                                             if n[0]>=60:
                                                 m=divmod(n[0],60)
                                                 print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                             else:

                                                 print("{}分{}秒".format(n[0],n[1]))
                                         else:
                                             print("{}秒".format(wl_time))
                                         while total_time-wl_time<rgv_ji:
                                                total_time+=1
                                                ok=True
                                         if ok==True and total_time-wl_time==rgv_ji:
                                                aim_wl=False
                                                gongxu[i]=1
                                                keep=i
                                                lock=True
                                                # print("一道工序完成",i)
                                                ok=False
                                                wl[i]=1
                                                aim=False
                                                finish[i]=0
                                                cnc_time[i]=total_time
                                                cnc_sign[i]=1
            for i in "cnk_1,cnk_3,cnk_5,cnk_7,cnk_2,cnk_4,cnk_6,cnk_8".split(",")[A:]:
                if jmp==True:
                    jmp=False
                    break
                elif total_time-cnc_time[i]>=cnc_two_two and huai[i]==0 and wl[i]==1:
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
                                             if wl[i]==1:
                                                 wl_time=total_time
                                                 if wl_time>=60:
                                                     n=divmod(wl_time,60)
                                                     if n[0]>=60:
                                                         m=divmod(n[0],60)
                                                         # print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                                     else:
                                                         pass
                                                         # print("{}分{}秒".format(n[0],n[1]))
                                                 else:
                                                     pass
                                                     # print("{}秒".format(wl_time))
                                                 while total_time-wl_time<rgv_ou:
                                                        total_time+=1
                                                        ok=True
                                                 if ok==True and total_time-wl_time==rgv_ou:
                                                        aim_wl=True
                                                        ok=False
                                                        wl[i]=1
                                                        if aim_made==True:
                                                            clear=total_time

                                                            while  total_time-clear<rgv_clear:
                                                                   total_time+=1
                                                                   ok=True
                                                            if ok==True and total_time-clear==rgv_clear:
                                                                   work+=1
                                                                   gongxu[i]=0
                                                                   aim_made=False
                                                                   finish[i]=0
                                                                   jmp=True
                                                                   aim=False
                                                                   wl[i]=0
                                                                   # print("第二道工序完成",i)
                                                                   # print("序列号：{},cnc号:{}".format(work,i))
                                                                   cnc_sign[i]=0
                    elif abs(cnc_set[i]-rgv_set)==2:
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
                                             if wl[i]==1:
                                                 wl_time=total_time
                                                 if wl_time>=60:
                                                     n=divmod(wl_time,60)
                                                     if n[0]>=60:
                                                         m=divmod(n[0],60)
                                                         # print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                                     else:
                                                         pass# print("{}分{}秒".format(n[0],n[1]))
                                                 else:
                                                     pass# print("{}秒".format(wl_time))
                                                 while total_time-wl_time<rgv_ou:
                                                        total_time+=1
                                                        ok=True
                                                 if ok==True and total_time-wl_time==rgv_ou:
                                                        aim_wl=True
                                                        ok=False
                                                        wl[i]=1
                                                        if aim_made==True:
                                                            clear=total_time

                                                            while  total_time-clear<rgv_clear:
                                                                   total_time+=1
                                                                   ok=True
                                                            if ok==True and total_time-clear==rgv_clear:
                                                                   work+=1
                                                                   gongxu[i]=0
                                                                   aim_made=False
                                                                   finish[i]=0
                                                                   jmp=True
                                                                   # print("第二道工序完成")
                                                                   aim=False
                                                                   wl[i]=0
                                                                   # print("序列号：{},cnc号:{}".format(work,i))
                                                                   cnc_sign[i]=0
                    elif  abs(cnc_set[i]-rgv_set)==3:
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
                                             if wl[i]==1:
                                                 wl_time=total_time
                                                 if wl_time>=60:
                                                     n=divmod(wl_time,60)
                                                     if n[0]>=60:
                                                         m=divmod(n[0],60)
                                                         # print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                                     else:
                                                         pass
                                                         # print("{}分{}秒".format(n[0],n[1]))
                                                 else:
                                                     pass
                                                     # print("{}秒".format(wl_time))
                                                 while total_time-wl_time<rgv_ou:
                                                        total_time+=1
                                                        ok=True
                                                 if ok==True and total_time-wl_time==rgv_ou:
                                                        aim_wl=True
                                                        ok=False
                                                        wl[i]=1
                                                        if aim_made==True:
                                                            clear=total_time

                                                            while  total_time-clear<rgv_clear:
                                                                   total_time+=1
                                                                   ok=True
                                                            if ok==True and total_time-clear==rgv_clear:
                                                                   work+=1
                                                                   gongxu[i]=0
                                                                   aim_made=False
                                                                   # print("第二道工序完成")
                                                                   finish[i]=0
                                                                   aim=False
                                                                   jmp=True
                                                                   wl[i]=0
                                                                   # print("序列号：{},cnc号:{}".format(work,i))
                                                                   cnc_sign[i]=0
                    elif  abs(cnc_set[i]-rgv_set)==0:
                            ok= False
                            aim=True
                            if aim==True:
                                             if wl[i]==1:
                                                 wl_time=total_time
                                                 if wl_time>=60:
                                                     n=divmod(wl_time,60)
                                                     if n[0]>=60:
                                                         m=divmod(n[0],60)
                                                         # print("{}时{}分{}秒".format(m[0],m[1],n[1]))
                                                     else:
                                                         pass
                                                         # print("{}分{}秒".format(n[0],n[1]))
                                                 else:
                                                     pass
                                                     # print("{}秒".format(wl_time))
                                                 while total_time-wl_time<rgv_ou:
                                                        total_time+=1
                                                        ok=True
                                                 if ok==True and total_time-wl_time==rgv_ou:
                                                        aim_wl=True
                                                        ok=False
                                                        wl[i]=1
                                                        if aim_made==True:
                                                            clear=total_time

                                                            while  total_time-clear<rgv_clear:
                                                                   total_time+=1
                                                                   ok=True
                                                            if ok==True and total_time-clear==rgv_clear:
                                                                   work+=1
                                                                   gongxu[i]=0
                                                                   # print("第二道工序完成")
                                                                   aim_made=False
                                                                   finish[i]=0
                                                                   aim=False
                                                                   jmp=True
                                                                   wl[i]=0
                                                                   # print("序列号：{},cnc号:{}".format(work,i))
                                                                   cnc_sign[i]=0
        total_time+=1
