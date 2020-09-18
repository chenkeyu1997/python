#!/usr/bin/python3

# -*- encoding: utf-8 -*-


class Lnode:
    def __init__(self, elem, next_=None):  ##初始化链表，并结点的next赋None
        self.elem = elem
        self.next = next_


llist1 = Lnode(1)  ##头结点
p = llist1
for i in range(2, 11):
    p.next = Lnode(i)  ##创建新的结点
    p = p.next

p = llist1  ###p重新指向表头   遍历所有的结点输出元素
while p is not None:
    print(p.elem)
    p = p.next