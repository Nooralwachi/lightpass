def crc(eids):
    print(eids)
    result = {}
    count =0
    for emp, reports in eids.items():
        if len(reports) >0:
            count += count_reports(emp, eids)
            result[emp] = count     
        result[emp] = count +1
        count =0
    print(result)

def count_reports(emp, eids):
    reports = eids[emp]
    for report in reports:
        return int(count_reports(report, eids)) + int(len(eids[emp]))
    else:
        return len(eids[emp]) 


crc({10: [20, 30],20: [40, 50],30: [],40: [],50: []})
crc({10: [20, 30], 20: [40], 30: [], 40: [50], 50:[] })