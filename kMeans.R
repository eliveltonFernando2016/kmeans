cl1 <- kmeans(obu1$rss, 5, nstart = 10)
plot(obu1$rss, col = cl1$cluster, pch=19)
points(cl1$centers, col = "grey", pch = 9, cex = 2)

cl1Jammer <- kmeans(OBU1jammer$rss, 5, nstart = 10)
plot(OBU1jammer$rss, col = cl1Jammer$cluster, pch=19)
points(cl1Jammer$centers, col = "grey", pch = 9, cex = 2)

cl10 <- kmeans(obu10$rss, 5, nstart = 10)
plot(obu10$rss, col = cl10$cluster, pch=19)
points(cl10$centers, col = "grey", pch = 9, cex = 2)

cl10Jammer <- kmeans(OBU10jammer$rss, 5, nstart = 10)
plot(OBU10jammer$rss, col = cl10Jammer$cluster, pch=19)
points(cl10Jammer$centers, col = "grey", pch = 9, cex = 2)

cl20 <- kmeans(obu20$rss, 5, nstart = 10)
plot(obu20$rss, col = cl20$cluster, pch=19)
points(cl20$centers, col = "grey", pch = 9, cex = 2)

cl20Jammer <- kmeans(OBU20jammer$rss, 5, nstart = 10)
plot(OBU20jammer$rss, col = cl20Jammer$cluster, pch=19)
points(cl20Jammer$centers, col = "grey", pch = 9, cex = 2)

cl40 <- kmeans(obu40$rss, 5, nstart = 10)
plot(obu40$rss, col = cl40$cluster, pch=19)
points(cl40$centers, col = "grey", pch = 9, cex = 2)

cl40Jammer <- kmeans(OBU40jammer$rss, 5, nstart = 10)
plot(OBU40jammer$rss, col = cl40Jammer$cluster, pch=19)
points(cl40Jammer$centers, col = "grey", pch = 9, cex = 2)

cl60 <- kmeans(obu60$rss, 5, nstart = 10)
plot(obu60[3:4], col = cl60$cluster, pch=19)
points(cl60$centers, col = "grey", pch = 9, cex = 2)

cl60Jammer <- kmeans(OBU60jammer$rss, 5, nstart = 10)
plot(OBU60jammer$rss, col = cl60Jammer$cluster, pch=19)
points(cl40Jammer$centers, col = "grey", pch = 9, cex = 2)

cl80 <- kmeans(obu80$rss, 5, nstart = 10)
plot(obu80$rss, col = cl80$cluster, pch=19)
points(cl80$centers, col = "grey", pch = 9, cex = 2)

cl80Jammer <- kmeans(OBU80jammer$rss, 5, nstart = 10)
plot(OBU80jammer$rss, col = cl80Jammer$cluster, pch=19)
points(cl80Jammer$centers, col = "grey", pch = 9, cex = 2)

cl100 <- kmeans(obu100$rss, 5, nstart = 10)
plot(obu100$rss, col = cl100$cluster, pch=19)
points(cl100$centers, col = "grey", pch = 9, cex = 2)

cl100Jammer <- kmeans(OBU100jammer$rss, 5, nstart = 10)
plot(OBU100jammer$rss, col = cl100Jammer$cluster, pch=19)
points(cl100Jammer$centers, col = "grey", pch = 9, cex = 2)