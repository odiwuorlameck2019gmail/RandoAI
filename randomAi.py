from datetime import datetime
import matplotlib.pyplot as plt 
import random 
import time
import mysql.connector as mysql 


try:
     conn=mysql.connect(user="root",password="tangimeko7583",host="localhost")
     print("Connection successful.")
except mysql.Error as err:
        print(""+err)
x_axis_data=[]
y_axis_data=[]     
plt.ion()
figure=plt.figure(facecolor="yellow")
x_axis=x_axis_data 
y_axis=y_axis_data  
plt.title("Stock Market Trend")
plt.xlabel('time')
plt.ylabel('Stock Market flow')
plt.grid(True)   
id=0
stock_status=""
count=0
#clearing chat data.
def clear_chat():  
        global count  
        if count==16:
                x_axis.clear()
                y_axis.clear() 
                plt.clf() 
                count=0
                plt.title("Stock Market Trend")
                plt.xlabel('time')
                plt.ylabel('Stock Market flow')
                plt.grid(True)  
        count+=1    


while True:
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        x_axis_data.append(current_time)    
        max_random=random.randrange(1,1000)             
        number=random.randrange(-1000,max_random)
        y_axis_data.append(number)
        #Add your random values to the database to create a dataset.
        cursor=conn.cursor()
        cursor.execute("USE RandomAI")
        cursor.execute("INSERT INTO PredictionValues(predictorValue) VALUES({})".format(number))
        conn.commit()
        circle=plt.Circle((current_time,number),0.2,color="b") 
        plt.plot(x_axis,y_axis,color="red")
       
        # draw chat  
        print("Current Trade value:{}".format(number)) 
        cursor.execute("SELECT id FROM PredictionValues WHERE predictorValue={}".format(number))         
        id_numeric_list=cursor.fetchall()
        predictions=[]
        for id_value in id_numeric_list:
                id=id_value[0]+1
                cursor.execute("SELECT predictorValue FROM PredictionValues WHERE id={}".format(id))
                prediction_values=cursor.fetchall()
                for p_value in prediction_values:
                             predictions.append(p_value[0])
        id=0   
        #Do something with the predictions .
        print("predictor Values:{}".format(predictions))
        
        if len(predictions)!=0:
                sum_predictions=0
                prediction_number=predictions
                for sum_p in prediction_number:
                     sum_predictions+=sum_p 
                     avarage_prediction=sum_predictions/len(predictions)
                sum_predictions=0
                
                p_number=avarage_prediction
                if p_number>number:
                        print("####################################")
                        print("#The Stock Market is Rising.^^^^^^^^#")
                        print("####################################")  
                else:   
                        print("####################################")
                        print("#The Stock  Market is Falling.!!!!!!#") 
                        print("####################################")
        else:
                print("Stock market Trend is loading prediction ,Please Wait For prediction")   
        predictions.clear()
        plt.gca().add_patch(circle)
        figure.canvas.draw()   
       
        figure.canvas.flush_events()                                                       
        # clear chat data.  
        clear_chat()   
        time.sleep(1.0)        
            
        
                              
