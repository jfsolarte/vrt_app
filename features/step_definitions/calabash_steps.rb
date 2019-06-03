require 'calabash-android/calabash_steps'

Then("I take picture") do
    screenshot_embed
end

When("I open the main menu") do
    perform_action('click_on_screen', 5, 5)
  end

When ("I open the overflow menu") do
    perform_action('click_on_screen', 95, 5)
  end

  When ("I press the next slide") do
    perform_action('click_on_screen', 95, 95)
  end

Then ("I touch the confirm link") do
    perform_action('click_on_screen', 80, 60)
  end

  Then ("I select the clear queue") do
    perform_action('click_on_screen', 80, 25)
  end

  Then(/I select "([^\"]*)"$/) do |identifier|
    tap_when_element_exists("* marked:'#{identifier}'")
  end

  Then ("I use scroll down") do
    # performAction('scroll_down')
    perform_action('drag', 70, 50, 30, 90, 10)
  end