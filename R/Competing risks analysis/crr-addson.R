##############################################################################
# Adds-on functions to crr() function in 'cmprsk' package by Gray, RJ. 
# Written by Luca Scrucca
#
# Reference: 
# Scrucca L, Santucci A, Aversa F (2009) Regression Modeling of Competing 
#   Risk Using R: An In Depth Guide for Clinicians. Submitted to Bone Marrow
#   Transplantation
##############################################################################

# This ensure that the package is loaded
if(!require(cmprsk))
  { stop("the package 'cmprsk' is required, please install it. \nSee help(install.packages).") }
  
factor2ind <- function(x, baseline)
{
# Given a factor variable x, create an indicator matrix of dimension 
# length(x) x (nlevels(x)-1) dropping the column corresponding to the 
# baseline level (by default the first level is used as baseline).
# Example:
# > x = gl(4, 2, labels = LETTERS[1:4])
# > factor2ind(x)
# > factor2ind(x, "C")
  xname <- deparse(substitute(x))
  n <- length(x)
  x <- as.factor(x)
  if(!missing(baseline)) x <- relevel(x, baseline)
  X <- matrix(0, n, length(levels(x)))
  X[(1:n) + n*(unclass(x)-1)] <- 1
  X[is.na(x),] <- NA
  dimnames(X) <- list(names(x), paste(xname, levels(x), sep = ":"))
  return(X[,-1,drop=FALSE])
}

modsel.crr <- function (object, ..., d = log(object$n)) 
{
  if(class(object) != "crr") 
    stop("object is not of class 'crr'")
  objects <- list(object, ...)
  nmodels <- length(objects)
  modnames <- paste("Model ", format(1:nmodels), ": ", 
                      lapply(objects, function(x) x$call), 
                      sep = "", collapse = "\n")
  # add null model
  mod0 <- object
  mod0$loglik <- mod0$loglik.null
  mod0$coef <- mod0$call$cov1 <- mod0$call$cov2 <- NULL
  objects <- c(list(mod0), objects)
  nmodels <- nmodels + 1
  #
  modnames <- c("Model 0: Null model", modnames)
  ns <- sapply(objects, function(x) x$n) 
  dfs <- sapply(objects, function(x) length(x$coef)) 
  if(any(ns != ns[1]))
    stop("models were not all fitted to the same dataset")
  out <- matrix(rep(NA, 5 * nmodels), ncol = 5)
  loglik <- sapply(objects, function(x) x$loglik)
  crit <- sapply(objects, function(x) -2*x$loglik + d*length(x$coef))
  out[,1] <- ns
  out[,2] <- loglik
  out[,3] <- dfs
  out[,4] <- crit
  out[,5] <- crit - min(crit)
  if(d==log(object$n)) critname <- "BIC"
  else if(d == 2) critname <- "AIC"
  else critname <- "Criterion"
  colnames(out) <- c("Num.obs", "logLik", "Df.fit", critname, paste(critname, "diff"))
  rownames(out) <- 0:(nmodels-1)
  title <- "Model selection table\n"
  topnote <- modnames
  structure(as.data.frame(out), heading = c(title, topnote), 
            class = c("anova", "data.frame"))
}
