# FOR POWER ONLY 
# FINAL BOXPLOT
# CLOSE AND OPEN TO SAVE LAST TEXT FILE
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import BoxplotLiveS as bp

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
            get_last_power=get_power[-1]  
            power_to_string = "{}".format(get_last_power)
            label_for_legend= "(Today) = "+power_to_string
            
            date_data_x= date_data_x+live_monday[0]+tuesday[0]+wednesday[0]+thursday[0]+friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+live_monday[1]+tuesday[1]+wednesday[1]+thursday[1]+friday[1]+saturday[1]+sunday[1]
            sns.boxplot(date_data_x,power_data_y,color="skyblue", zorder=0)
            plt.scatter("Monday",get_last_power, color="green",marker='^',s=100, label=label_for_legend, zorder=1)

        elif day_of_week=="Tuesday":
            live_tuesday= bp.Tuesday()
            get_power=live_tuesday[1]
            get_last_power=get_power[-1]  
            power_to_string = "{}".format(get_last_power)
            label_for_legend= "(Today) = "+power_to_string
            
            date_data_x= date_data_x+monday[0]+live_tuesday[0]+wednesday[0]+thursday[0]+friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+live_tuesday[1]+wednesday[1]+thursday[1]+friday[1]+saturday[1]+sunday[1]
            sns.boxplot(date_data_x,power_data_y,color="skyblue",zorder=1)
            sns.swarmplot(date_data_x,power_data_y, color='green', zorder=2)
            plt.scatter("hey",0,s=0.001,zorder=0)#X
            plt.scatter("Tuesday",get_last_power, color="green",marker='^',s=100, label=label_for_legend, zorder=3, edgecolors='black')
            
        elif day_of_week=="Wednesday":
            live_wednesday= bp.Wednesday()
            date_data_x= date_data_x+monday[0]+tuesday[0]+live_wednesday[0]+thursday[0]+friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+live_wednesday[1]+thursday[1]+friday[1]+saturday[1]+sunday[1]
            sns.boxplot(date_data_x,power_data_y)
                        
        elif day_of_week=="Thursday":
            live_thursday= bp.Thursday()
            date_data_x= date_data_x+monday[0]+tuesday[0]+wednesday[0]+live_thursday[0]+friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+wednesday[1]+live_thursday[1]+friday[1]+saturday[1]+sunday[1]
            sns.boxplot(date_data_x,power_data_y)
                         
        elif day_of_week=="Friday":
            live_friday= bp.Friday()
            date_data_x= date_data_x+monday[0]+tuesday[0]+wednesday[0]+thursday[0]+live_friday[0]+saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+wednesday[1]+thursday[1]+live_friday[1]+saturday[1]+sunday[1]
            sns.boxplot(date_data_x,power_data_y)
                                
        elif day_of_week=="Saturday":
            live_saturday= bp.Saturday()
            date_data_x= date_data_x+monday[0]+tuesday[0]+wednesday[0]+thursday[0]+friday[0]+live_saturday[0]+sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+wednesday[1]+thursday[1]+friday[1]+live_saturday[1]+sunday[1]
            sns.boxplot(date_data_x,power_data_y)

        elif day_of_week=="Sunday":
            live_sunday= bp.Sunday()
            date_data_x= date_data_x+monday[0]+tuesday[0]+wednesday[0]+thursday[0]+friday[0]+saturday[0]+live_sunday[0]
            power_data_y= power_data_y+monday[1]+tuesday[1]+wednesday[1]+thursday[1]+friday[1]+saturday[1]+live_sunday[1]
            sns.boxplot(date_data_x,power_data_y)
            
        plt.legend(loc="upper right")        
        print(i)   
        print(date_data_x, power_data_y)                        
    ani = FuncAnimation(plt.gcf(), animate, interval= 60000)
    plt.tight_layout()

    plt.show()
    
if __name__ == "__main__":
    main()


#if tuesday_plot():   at the end    day_string= "tuesday"
# done
# if day_of_week!= day_string: balik sa main para magcompute lahat ng data ulit(refresh)
