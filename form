require 'form_api'

client = FormAPI::Client.new
response = client.generate_pdf(
  template_id: 'YOUR_TEMPLATE_ID',
  test: true,
  data: { first_name: 'John', last_name: 'Smith' },
  metadata: { user_id: 123 }
)
puts "Download your PDF at: #{response.submission.download_url}"
