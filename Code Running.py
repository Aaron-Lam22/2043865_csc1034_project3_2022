from MainCode import *

catagoriesCSV()

ViewClients()

addClient('Rev', 'Darby', 'Pansie', 'She/Her', 'pansiedarbr@email.com', '1967-07-20', 'preacher', '2000.00', '100' )
addClient('Mr', 'Penuel', 'Dave', 'He/Him', 'davep123@mailing.com', '1973-05-23', 'Diplomat', '4362.11', '1000')

ViewClients()

addClient('Mrs', 'Leary', 'Rainy', 'She/Her', 'rainyl@email.com', '1975-09-12', 'Teacher', '1230.45', '100' )
addClient('Mr', 'Glade', 'Fruman', 'He/Him', 'epicman23@mailing.com', '1990-12-23', 'Youtuber', '4362.11', '1000')

changeMoney(3, -475.33)

searchByDOB('1967-07-20')

ViewClients()