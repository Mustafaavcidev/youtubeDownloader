from pytube import YouTube

url = input("enter videos url : ")

YouTube(url).streams.first().download('')

