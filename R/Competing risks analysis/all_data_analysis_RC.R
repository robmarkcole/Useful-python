setwd("~/Documents/Github/Useful-python-for-medical-physics/R/Competing risks analysis")
# All 211 patients
#all_data_RC <- read.csv("~/Documents/Github/Useful-python-for-medical-physics/R/Competing risks analysis/all_data_RC.csv")

# Drop 8 PB patients
#all_data_RC <- read.csv("~/Documents/Github/Useful-python-for-medical-physics/R/Competing risks analysis/all_data_RC_drop_8PB.csv")

# Drop 32 PB patients
#all_data_RC <- read.csv("~/Documents/Github/Useful-python-for-medical-physics/R/Competing risks analysis/all_data_RC_drop_32PB.csv")


# include 3 equal competing events (cat 2)
# all_data_RC <- read.csv("~/Documents/Github/Useful-python-for-medical-physics/R/Competing risks analysis/all_data_RC_with_competing.csv")

# include significantly more competing events to PB
all_data_RC <- read.csv("~/Documents/Github/Useful-python-for-medical-physics/R/Competing risks analysis/all_data_RC_with_competing2.csv")


attach(all_data_RC)
dis=factor(dis, levels= c(0,1), labels =c("CCC", "PB")) 
table(dis, status)  # see summary of data
tapply(ftime, list(dis, status), mean)
source ("CumIncidence.R")  # import
fit=CumIncidence (ftime, status, dis, cencode = 0, xlab="Months")