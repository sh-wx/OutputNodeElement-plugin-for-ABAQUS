# OutputNodeElement-plugin-for-ABAQUS
Output Node&amp;Element after assembly in ABAQUS

Part在组装后可以进行任意的旋转和平移，在完成旋转和平移后就可以利用这个插件输出节点和单元信息了。如果需要针对移动后的part做手脚，便不再需要研究复杂的坐标变换。

前提是需要有网格，在mesh后需要切换到其他模块来更新数据库才能被识别网格。不过，还有个缺点，part中只能有一种单元类型，比如都是C3D10或者都是C3D8，因为element中不同单元类型是分开放置的。
