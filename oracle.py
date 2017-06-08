import cx_Oracle


def connect(username, password, hostname, port, servicename):
    try:
        db = cx_Oracle.connect(username, password, hostname + ':' + port + '/' + servicename)
    except cx_Oracle.DatabaseError as e:
        print('Database connection error: %s'.format(e))
        exit(0)
    return db


def do_actions(db, test_id):
    cursor = db.cursor()
    # 插入一条记录
    sql = 'insert into WAREHOUSES values (' + str(test_id) + ', \'wl\',' + str(test_id) + ')'
    cursor.execute(sql)

    # 查询是否增加成功
    sql = 'select * from WAREHOUSES where WAREHOUSE_ID=' + str(test_id)
    x = cursor.execute(sql)
    res = x.fetchall()
    print(res)

    # 更新记录
    sql = 'update WAREHOUSES set LOCATION_ID=' + str(test_id-1000) + 'where WAREHOUSE_ID=' + str(test_id)
    cursor.execute(sql)
    sql = 'select * from WAREHOUSES where WAREHOUSE_ID=' + str(test_id)
    x = cursor.execute(sql)
    res = x.fetchall()
    print(res)

    #删除记录
    sql = 'delete from WAREHOUSES where WAREHOUSE_ID=' + str(test_id)
    cursor.execute(sql)
    sql = 'select * from WAREHOUSES where WAREHOUSE_ID=' + str(test_id)
    x = cursor.execute(sql)
    res = x.fetchall()
    print(res)

    cursor.close()


def main():
    try:
        db = connect('soe', 'soe', '10.32.128.141', '1521', 'dba')
        do_actions(db, 1978)
    finally:
        db.close()
        print('Close db conn')


if __name__ == '__main__':
    main()
