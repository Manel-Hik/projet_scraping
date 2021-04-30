# -*- coding: utf-8 -*-
import scrapy


class AllInfosSpider(scrapy.Spider):
    name = 'all_infos'
    allowed_domains = ['www.udemy.com']
    start_urls = ['https://www.udemy.com/courses/personal-development']

    def parse(self, response):
        
        courses = response.xpath("response.get(//div[@class='filter-container--container--3A8k6']/div[@class='course-list--container--3zXPS']/div[@class='popper--popper--19faV popper--popper-hover--4YJ5J']")
        for course in courses:
            yield {

                'course_title' : course.xpath(".//div[@class='udlite-focus-visible-target udlite-heading-md course-card--course-title--2f7tE']/text()").get(),
                
                'course_link' : course.xpath(".//a/@href").get(),

                'course_description' : course.xpath(".//p[@class='udlite-text-sm course-card--course-headline--yIrRk']/text()").get(),

                'instructors' : course.xpath(".//div[@class='udlite-text-xs course-card--instructor-list--lIA4f']/text()").get(),

            }
        #next_page = response.urljoin(response.xpath("//a[@class='button button--primary next-page']/@href").get())
        
        #next_page = response.xpath("//a[@class='button button--primary next-page']/@href").get()

        #if next_page:
            #yield scrapy.Request(url=next_page , callback = self.parse,dont_filter = True 
                               # )


                

            # 1/ absolute_url = f"https://worldometers.info{link}"
            # 2 absolute_url = response.urljoin(link)


            
            #yield response.follow(url=link, callback = self.parse_course,meta = {'course_title':course_title})


        #next_page = response.urljoin(response.xpath("//a[@class='udlite-btn udlite-btn-medium udlite-btn-ghost udlite-heading-sm pagination--page--3FKqV']/@href").get())
        #if next_page < 10:
         #   yield scrapy.Request(url=next_page , callback = self.parse,dont_filter = True)
                                

"""
    def parse_course(self, response):
        name = response.request.meta['course_title']
        course_info = response.xpath("//*[@id='udemy']/div[2]/div[3]/div[1]/div[3]/div/div")
        for inf in course_info:

            course_descrip = inf.xpath(".//div[4]/div/div[1]/div[1]/div/text()").get()

            language = inf.xpath(".//div[4]/div/div[1]/div[4]/div[2]/text()")

            rating = inf.xpath(".//div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div/span/span[1]/text()").get()

            total_rating = inf.xpath(".//div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div/text()").get()

            Nb_student_subsribed = inf.xpath(".//div[4]/div/div[1]/div[2]/div[2]/div[2]/div/text()").get()

            price = inf.xpath(".//div[5]/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/span[2]/span/text()").get()

            yield {
                'course_title':course_title,
                'language': language,
                'course_descrip' : course_descrip,
                'rating' : rating,
                'total_rating' : total_rating,
                'Nb_student_subsribed':Nb_student_subsribed,
                'price': price
                
                }
"""