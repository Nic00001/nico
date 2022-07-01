#boxplotliveF ver2
# FOR POWER ONLY 
# FINAL BOXPLOT
# CLOSE AND OPEN TO SAVE LAST TEXT FILE
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import BoxplotLiveSver2 as bp
#plt.style.use('fivethirtyeight')
plt.style.use('seaborn-whitegrid')

def main():
    monday= bp.Monday()
    tuesday= bp.Tuesday()  
    wednesday= bp.Wednesday()
    thursday= bp.Thursday()
    friday= bp.Friday()
    saturday= bp.Saturday()
    sunday= bp.Sunday()
    
    def animate(i):
        date_data_x=[]
        power_data_y=[]
        
        day_of_week=datetime.today().strftime('%A')
        plt.clf()
        plt.title('  P O W E R  ',fontsize=20, fontweight='bold')
        
        if day_of_week=="Monday":
            live_monday= bp.Monday()
            get_power=live_monday[1]
            get_yesterday_power= sunday[1]
            date_data_x= date_data_x+live_monday[0]+tuesday[0]+wednesday[0]+thursday[0]+friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+live_monday[1]+tuesday[1]+wednesday[1]+thursday[1]+friday[1]+saturday[1]+sunday[1]
        
        elif day_of_week=="Tuesday":
            live_tuesday= bp.Tuesday()
            get_power=live_tuesday[1]
            get_yesterday_power=monday[1]
            date_data_x= date_data_x+monday[0]+live_tuesday[0]+wednesday[0]+thursday[0]+friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+live_tuesday[1]+wednesday[1]+thursday[1]+friday[1]+saturday[1]+sunday[1]
            plt.scatter("hey",0,s=0.001,zorder=0)#X
            
        elif day_of_week=="Wednesday":
            live_wednesday= bp.Wednesday()
            get_power=live_wednesday[1]
            get_yesterday_power= tuesday[1]
            
            date_data_x= date_data_x+monday[0]+tuesday[0]+live_wednesday[0]+thursday[0]+friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+live_wednesday[1]+thursday[1]+friday[1]+saturday[1]+sunday[1]
            plt.scatter(["blank","blank1"],[0,0],s=0.001,zorder=0)#X
                
        elif day_of_week=="Thursday":
            live_thursday= bp.Thursday()
            get_power=live_thursday[1]
            get_yesterday_power= wednesday[1]
            date_data_x= date_data_x+monday[0]+tuesday[0]+wednesday[0]+live_thursday[0]+friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+wednesday[1]+live_thursday[1]+friday[1]+saturday[1]+sunday[1]
            plt.scatter(["blank","blank1","blank2"],[0,0,0],s=0.001,zorder=0)#X
                   
        elif day_of_week=="Friday":
            live_friday= bp.Friday()
            get_power=live_friday[1]
            get_yesterday_power= thursday[1]
            date_data_x= date_data_x+monday[0]+tuesday[0]+wednesday[0]+thursday[0]+live_friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+wednesday[1]+thursday[1]+live_friday[1]+saturday[1]+sunday[1]
            plt.scatter(["blank","blank1","blank2","blank3"],[0,0,0,0],s=0.001,zorder=0)#X
      
        elif day_of_week=="Saturday":
            live_saturday= bp.Saturday()
            get_power=live_saturday[1]
            get_yesterday_power= friday[1]
            date_data_x= date_data_x+monday[0]+tuesday[0]+wednesday[0]+thursday[0]+friday[0]+live_saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+wednesday[1]+thursday[1]+friday[1]+live_saturday[1]+sunday[1]
            plt.scatter(["blank","blank1","blank2","blank3","blank4"],[0,0,0,0,0],s=0.001,zorder=0)#X

        elif day_of_week=="Sunday":
            live_sunday= bp.Sunday()
            get_power=live_sunday[1]
            get_yesterday_power= saturday[1]
            date_data_x= date_data_x+monday[0]+tuesday[0]+wednesday[0]+thursday[0]+friday[0]+saturday[0]+live_sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+wednesday[1]+thursday[1]+friday[1]+saturday[1]+live_sunday[1]            
            plt.scatter(["blank","blank1","blank2","blank3","blank4","blank5"],[0,0,0,0,0,0],s=0.001,zorder=0)#X
           

        get_last_power=get_power[-1]
        get_yesterday_power_fin =get_yesterday_power[-1]
        power_to_string = "{}".format(get_last_power)
        power_to_string_yesterday= "{}".format(get_yesterday_power_fin)
        #label_for_legend_yesterday="(Yesterday) = "+power_to_string_yesterday
        label_for_legend= "\n(Today)       = "+power_to_string+"\n(Yesterday) = "+power_to_string_yesterday
        
        sns.boxplot(date_data_x,power_data_y,color="skyblue",zorder=1)
        #sns.swarmplot(date_data_x,power_data_y, color='green', zorder=2)
        
        if get_last_power>get_yesterday_power_fin:
            plt.scatter("filler",get_last_power, color="green",marker='^',s=100, label=label_for_legend, zorder=3, edgecolors='black')
        else:
            plt.scatter("filler",get_last_power, color="red",marker='v',s=100, label=label_for_legend, zorder=3, edgecolors='black')

 
        plt.legend(loc="upper right",prop={'size': 15})      
        
    ani = FuncAnimation(plt.gcf(), animate, interval= 60000)
    plt.tight_layout()

    plt.show()
    
if __name__ == "__main__":
    main()

#if tuesday_plot():   at the end    day_string= "tuesday"
# done
# if day_of_week!= day_string: balik sa main para magcompute lahat ng data ulit(refresh)
