-- Truy suất tổng hoa hồng (commission) cho mỗi thành phố (city)

select s.city, sum(s.commission) sum_of_commission
from salesman s
group by s.city

-- Truy suất tất cả khách hàng (customer) mà có người môi giới (sales_man) tương ứng có hoa hồng
-- >0,12, sắp xếp theo hoa hồng 

select * from customer c
join salesman s on c.salesman_id = s.salesman_id
where s.commission > 0.12 
order by s.commission