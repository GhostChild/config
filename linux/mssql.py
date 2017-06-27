# -*- coding: utf-8 -*-
import pymssql


class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
    
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
      
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()


        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


ms=MSSQL("192.168.0.107","sa","845685","isszmv9")



import csv

with open("vip.csv","r",encoding='utf8') as csvfile:
    sreader=csv.DictReader(csvfile)

    for row in sreader:
        card_id=row['card_id']
        card_no=row['card_id']
        card_type=row['card_type']
        vip_name=row['vip_name']
        now_acc_num=row['integral_inout']
        acc_num=row['vip_integral']
        spare_cash=row['spare_cash']
        birthday=row['birthday']
        mobile=row['vip_tel']

        if len(vip_name)>4:
            vip_name=vip_name[0:3]

        if card_type=='02':
            card_type='0'
        elif card_type=='01':
            card_type='1'
        elif card_type=='03':
            card_type='2'
        elif card_type=='04':
            card_type='3'
        elif card_type=='06':
            card_type='4'
        elif card_type=='05':
            card_type='5'
        elif card_type=='07':
            card_type='6'

        #print(card_id,card_no,card_type,vip_name,now_acc_num,acc_num,birthday,mobile,spare_cash)
        _card_id="'%s'"%(card_id)
        _card_no="'%s'"%(card_id)
        _card_type="'%s'"%(card_type)
        _vip_name="'%s'"%(vip_name)
        _card_status="'0'"
        _oper_id="'1001'"
        _oper_date="'2017-5-15 00:00:00.000'"
        _now_acc_num="'%s'"%(now_acc_num)
        _acc_num="'%s'"%(acc_num)
        _dec_num="'0'"
        _save_amt = "'%s'" % (spare_cash)
        _birthday="'%s'"%(birthday)
        _mobile="'%s'"%(mobile)
        _send_amt="'0'"

        str="insert into t_rm_vip_info (card_id,card_no,card_type,vip_name,card_status,oper_id,oper_date,now_acc_num,acc_num,dec_num,save_amt,birthday,mobile,send_amt)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(_card_id,_card_no,_card_type,_vip_name,_card_status,_oper_id,_oper_date,_now_acc_num,_acc_num,_dec_num,_save_amt,_birthday,_mobile,_send_amt)
        print(str)
        reslist=ms.ExecNonQuery(str.encode("utf8"))










# print(str)
#reslist=ms.ExecNonQuery("insert into t_rm_vip_info (card_id,card_no,card_type,vip_name,card_status,oper_id,oper_date,now_acc_num,acc_num,dec_num,birthday,mobile,send_amt)VALUES (%s,)"%("_card_no"))
# str="update t_rm_vip_info set birthday=%s where card_id='0000001'"%(_birthday)
#reslist=ms.ExecNonQuery("insert into t_rm_vip_info (card_id,card_no,card_type,vip_name,card_status,oper_id,oper_date,now_acc_num,acc_num,dec_num,birthday,mobile,send_amt)VALUES ('23333','23333','0','yuki','0','1001','2017-5-15 00:00:00.000','2333','2333','0','2017-5-15 00:00:00.000','13333900138','0')")

#reslist=ms.ExecQuery("select * from t_rm_vip_info".encode("utf8"))

#print(str)


# for n in reslist:
#     print(n[3])
