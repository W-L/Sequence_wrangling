#plot the GC content for all windows
library(ggplot2)
args<-commandArgs(TRUE)

GC_path<-args[1]
GC_frame<-read.csv(GC_path,sep="")

med<-median(GC_frame$GC)

pdf(file=paste(GC_path,".pdf",sep=""),width=20)

ggplot(GC_frame, aes(x=names, y=GC,group=1)) + 
  #geom_point(size=1,shape=19) +
  geom_line(size=.1) +
  ylab("GC content (%)") +
  xlab("") +
  geom_hline(yintercept = med, linetype="dashed") +
  annotate("text", x=200, y=10, label=paste("median=",round(med,2),sep="")) +
  annotate("text", x=200, y=55, label=GC_path) +
  theme(axis.text.x = element_blank())

dev.off()
