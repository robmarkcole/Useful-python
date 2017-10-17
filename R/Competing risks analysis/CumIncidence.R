#############################################################################
#                                                                           #
#                 CUMULATIVE INCIDENCE CURVES IN R                          #
#                                                                           #
# Written by Luca Scrucca                                                   #
#                                                                           #
# Reference:                                                                #
# Scrucca L., Santucci A., Aversa F. (2007) Competing risks analysis using  #
#   R: an easy guide for clinicians. Bone Marrow Transplantation, 40,       #
#   381--387.                                                               #
#############################################################################
# ver. 1.1 Feb 2008
#          - allow group to be missing
#          - if t is provided both computation and plots use t as time points
#          - allow col, lwd to be used for curves with confidence bands
#          - fix some bugs in the legend
#          - added help on source code
# ver. 1.0 May 2007
#          - Version appearing in the BMT paper
#############################################################################
#
# Usage:
# 
#   CumIncidence(ftime, fstatus, group, t, strata, rho = 0, cencode = 0,
#             	 subset, na.action = na.omit, level, 
#                xlab = "Time", ylab = "Probability", 
#                col, lty, lwd, digits = 4)
# 
# Arguments:
# 
# ftime = failure time variable.
# fstatus = variable with distinct codes for different causes of 
#           failure and also a distinct code for censored observations.
# group	= estimates will be calculated within groups given by distinct 
#         values of this variable. Tests will compare these groups. If 
#         missing then treated as all one group (no test statistics).
# t = a vector of time points where the cumulative incidence function 
#     should be evaluated.
# strata = stratification variable. Has no effect on estimates. Tests 
#          will be stratified on this variable. (all data in 1 stratum,
#          if missing).
# rho = power of the weight function used in the tests. By default is 
#       set to 0.
# cencode = value of fstatus variable which indicates the failure time
#           is censored.
# subset = a logical vector specifying a subset of cases to include in 
#          the analysis.
# na.action = a function specifying the action to take for any cases 
#             missing any of ftime, fstatus, group, strata, or subset. 
#             By default missing cases are omitted.
# level = a value in the range [0,1] specifying the level for pointwise
#         confidence bands.
# xlab = text for the x-axis label.
# ylab = text for the y-axis label.
# col = color(s) used for plotting curves (see plot.default).
# lty = line type(s) used for plotting curves (see plot.default).
# lwd = line width(s) used for plotting curves (see plot.default).
# digits = number of significant digits used for printing values. By 
#          default set at 4.
# 
#############################################################################

"CumIncidence" <- function(ftime, fstatus, group, t, strata, rho = 0, 
	                         cencode = 0, subset, na.action = na.omit, level,
	                         xlab = "Time", ylab = "Probability", 
	                         col, lty, lwd, digits = 4)
{
  # check for the required package
  if(!require("cmprsk"))
    { stop("Package `cmprsk' is required and must be installed.\n 
           See help(install.packages) or write the following command at prompt
           and then follow the instructions:\n
           > install.packages(\"cmprsk\")") } 
  # collect data
  mf  <- match.call(expand.dots = FALSE)
  mf[[1]] <- as.name("list")
  mf$t <- mf$digits <- mf$col <- mf$lty <- mf$lwd <- mf$level <- 
  mf$xlab <- mf$ylab <- NULL
  mf <- eval(mf, parent.frame())
  g <- max(1, length(unique(mf$group)))
  s <- length(unique(mf$fstatus))
  if(missing(t)) 
    { time <- pretty(c(0, max(mf$ftime)), 6)
      ttime <- time <- time[time < max(mf$ftime)] }
  else { ttime <- time <- t }
  # fit model and estimates at time points
  fit   <- do.call("cuminc", mf)
  tfit <- timepoints(fit, time)
  # print result
  cat("\n+", paste(rep("-", 67), collapse=""), "+", sep ="")
  cat("\n| Cumulative incidence function estimates from competing risks data |")
  cat("\n+", paste(rep("-", 67), collapse=""), "+\n", sep ="")
  tests <- NULL
  if(g > 1)
    { tests <- fit$Tests
	    colnames(tests) <- c("Statistic", "p-value", "df")
      cat("Test equality across groups:\n")
      print(tests, digits = digits) }
  cat("\nEstimates at time points:\n")
  print(tfit$est, digits = digits)
  cat("\nStandard errors:\n")
  print(sqrt(tfit$var), digits = digits)
  #
  if(missing(level))
    { # plot cumulative incidence functions
      if(missing(t))
        { time <- sort(unique(c(ftime, time)))
          x <- timepoints(fit, time) }
      else x <- tfit
      col <- if(missing(col)) rep(1:(s-1), rep(g,(s-1))) else col
      lty <- if(missing(lty)) rep(1:g, s-1) else lty
      lwd <- if(missing(lwd)) rep(1, g*(s-1)) else lwd      
      matplot(time, base::t(x$est), type="s", ylim = c(0,0.4),   # c(0,1)
              xlab = xlab, ylab = ylab, xaxs="i", yaxs="i", 
              col = col, lty = lty, lwd = lwd)
      legend("topleft", legend =  rownames(x$est), x.intersp = 2, 
             bty = "n", xjust = 1, col = col, lty = lty, lwd = lwd)
      out <- list(test = tests, est = tfit$est, se = sqrt(tfit$var))
    }
  else
    { if(level < 0 | level > 1) 
        error("level must be a value in the range [0,1]")
      # compute pointwise confidence intervals
      oldpar <- par(ask=TRUE)
      on.exit(par(oldpar))
      if(missing(t))
        { time <- sort(unique(c(ftime, time)))
          x <- timepoints(fit, time) }
      else x <- tfit
      z <- qnorm(1-(1-level)/2)
      lower <- x$est ^ exp(-z*sqrt(x$var)/(x$est*log(x$est)))
      upper <- x$est ^ exp(z*sqrt(x$var)/(x$est*log(x$est)))
      col <- if(missing(col)) rep(1:(s-1), rep(g,(s-1))) 
             else             rep(col, g*(s-1))
      lwd <- if(missing(lwd)) rep(1, g*(s-1)) 
             else             rep(lwd, g*(s-1))      
      # plot pointwise confidence intervals
      for(j in 1:nrow(x$est))
         { matplot(time, cbind(x$est[j,], lower[j,], upper[j,]), type="s", 
                   xlab = xlab, ylab = ylab, xaxs="i", yaxs="i", 
                   ylim = c(0,1), col = col[j], lwd = lwd[j], lty = c(1,3,3))
           legend("topleft", legend =  rownames(x$est)[j], bty = "n", xjust = 1) }
      # print pointwise confidence intervals
      i <- match(ttime, time)
      ci <- array(NA, c(2, length(i), nrow(lower)))
      ci[1,,] <- base::t(lower[,i])
      ci[2,,] <- base::t(upper[,i])
      dimnames(ci) <- list(c("lower", "upper"), ttime, rownames(lower))
      cat(paste("\n", level*100, "% pointwise confidence intervals:\n\n", sep=""))
      print(ci, digits = digits)
      out <- list(test = tests, est = x$est, se = sqrt(tfit$var), ci = ci)
    }
  # return results
  invisible(out)
}
